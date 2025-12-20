"""
Docstring for ParseData

"""

import os

# collect_data_files()
from collections import defaultdict  # findTargetFile()
from typing import Dict, List

import pandas as pd


def categorize_files_by_extension(
    file_extensions: List[str],
    folder_input: str,
) -> Dict[str, List[str]]:
    """
    Categorize all files under ${folder_input} by ${file_extensions}

    Args:
        file_extensions (List[str]): Required file extensions
        folder_input (str): The target folder

    Returns:
        Dict[str List[str]]: format(file_extension, files_path)
    """
    try:
        all_files: List[str] = os.listdir(folder_input)
    except FileNotFoundError:
        return {}

    tmp_dict: Dict[str, List[str]] = defaultdict(list)

    for file_name in all_files:
        for extension in file_extensions:
            if file_name.endswith(extension):
                tmp_dict[extension].append(os.path.join(folder_input, file_name))

    return dict(tmp_dict)


def valid_xls_file(
    file_path: str,
) -> str:
    """
    Check the xls file is valid

    Args:
        file_path (str): The file location

    Returns:
        str: The real file extension of xls file
    """
    with open(file_path, "rb") as f:
        head = f.read(64).lower()

    if b"<html" in head or b"<!doctype html" in head:
        return "html"

    # BIFF .xls magic bytes: D0 CF 11 E0 (OLE2)
    if head.startswith(b"\xd0\xcf\x11\xe0"):
        return "xls"

    return "unknown"


def parse_target_file_by_extension(
    file_paths_by_ext: Dict[str, List[str]],
) -> Dict[str, List[pd.DataFrame]]:
    """
    Parse files and return as pd.DataFrame by file extension

    Args:
        file_paths_by_ext (Dict[str, List[str]]): (file_extension, files_path)

    Raises:
        RuntimeError: When get unsupport extension

    Returns:
        Dict[str, List[pd.DataFrame]]: (file_extension, pd.DataFrame of each file)
    """
    tmp_dict: Dict[str, List[pd.DataFrame]] = defaultdict(list)

    for file_extension, paths in file_paths_by_ext.items():
        print(f"{file_extension}, have {len(paths)} files")
        for file_path in paths:
            if not file_path:
                continue
            if not os.path.isfile(file_path):
                print(f"Warning: path not found or not a file: {file_path}")
                continue

            if file_extension == ".xls":
                # [Issue] Fix the read failed on the fake xls files
                #         (sometime .html save as .xls)
                real_extension = valid_xls_file(file_path)
                print(f"Reading: {file_path}, {real_extension}")

                if real_extension == "html":
                    print(f"[HTML] {file_path}")
                    list_df: List[pd.DataFrame] = pd.read_html(file_path)  # pyright: ignore[reportUnknownMemberType]
                    # keep html tables as a list of DataFrames
                    tmp_dict["html"].extend(list_df)

                elif real_extension == "xls":
                    print(f"[XLS] {file_path}")
                    df: pd.DataFrame = pd.read_excel(file_path, engine="xlrd")  # pyright: ignore[reportUnknownMemberType]
                    tmp_dict["xls"].append(df)
                else:
                    raise RuntimeError(
                        f"Unsupported extension: {file_path} {real_extension}"
                    )

    return tmp_dict


def load_data_by_extension(
    folder_input: str,
    file_extension: List[str],
) -> Dict[str, List[pd.DataFrame]]:
    """
    Read the ${file_extension} extension file under the ${folder_input} folder \n
    And return the pd.DataFrame by different file extensions

    Args:
        folder_input (str): The folder path of duplicate files
        file_extension (List[str]): The target file extensions

    Returns:
        Dict[str, List[pd.DataFrame]]: (file_extension, pd.DataFrame of each file)
    """

    file_paths_by_ext: Dict[str, List[str]] = categorize_files_by_extension(
        file_extension,
        folder_input,
    )

    return parse_target_file_by_extension(file_paths_by_ext)
