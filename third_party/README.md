### Build the wheel for the wxPython=4.2.4

```shell
## Build images
podman build -f dockerfile.wxPython -t build_wxpython

## run the container and get the wheel
mkdir wxPython
podman run --rm -v $(pwd)/wxPython:/build build_wxpython

## add the uv environment
cd .. # back to root of the repository
uv add --active ./third_party/wxPython/wheels/wxpython-4.2.4-cp313-cp313-linux_x86_64.whl

```


