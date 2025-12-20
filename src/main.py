"""
Docstring for main
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List

import pandas as pd

# self lib
from ParseData import load_data_by_extension


def duplicate_source_files(
    src_path: str,
    dst_path: str,
    file_extensions: List,
):
    """
    Copy the source files to workspace

    Args:
        src_path (str): The source path of files
        dst_path (str): The destination path of duplicate files
        file_extensions (List): The target file extensions
    """
    src_dir = Path(src_path)
    dst_dir = Path(dst_path)

    for file in src_dir.glob("*"):
        if file.suffix.lower() in file_extensions:
            shutil.copy2(file, dst_dir / file.name)


def main():
    # To-do [GUI]  Replace with user input
    #        1. Note! Copy from the source, DO NOT operate the source directly
    folder_source: str = "/home/james/Downloads/Zenfone 10/"
    folder_input: str = "./Input"
    folder_output: str = "./Output"
    file_extensions: List = [".xls"]  # , ".txt"

    # Generate the Input/Output folder for dataset
    os.makedirs(folder_input, exist_ok=True)
    os.makedirs(folder_output, exist_ok=True)

    # Copy specific ${file_extensions} files under ${folder_source} to ${folder_input}
    duplicate_source_files(folder_source, folder_input, file_extensions)

    # Let the data combine to a List[pd.DataFrame]
    raw_data_by_extension: Dict[str, List[pd.DataFrame]] = load_data_by_extension(
        folder_input, file_extensions
    )

    ## print data
    for file_ext, df_list in raw_data_by_extension.items():
        print(f"\n{'=' * 20} {file_ext.upper()} TABLES ({len(df_list)}) {'=' * 20}")

        if not df_list:
            print("  No tables found.")
            continue

        for i, df in enumerate(df_list):
            print(f"\n[Table {i + 1}]")
            # print first 3 line
            print(df.head(3))
            print(f"Shape: {df.shape}")

    # To-do [GUI] Clean data
    #        1. Show the data on the GUI
    #        2. User selects the data they need on the GUI
    #           drop the duplicate data
    #        3-1. Save the data as csv
    #        3-2. Pass the pd.DataFrame to the plot API() to draw the figure

    # save data as csv
    # combined_df: pd.DataFrame = (
    #     pd.concat(ls_data, ignore_index=True).drop_duplicates().reset_index(drop=True)
    # )
    # combined_df.to_csv(folder_output + "/AllData.csv", index=False)

    # To-do [Plot] Pass the combined pd.DataFrame to plot API()


if __name__ == "__main__":
    main()
