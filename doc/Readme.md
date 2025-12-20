### Build the docker/podman image
```shell
# Build with default doxygen version
podman build -t doxygen_py3.13 -f ./doc/dockerfile

## or

# Build with specifix doxygen version
podman build -t doxygen_py3.13 --build-arg DOXYGEN_VERSION=1.15.0 -f ./doc/dockerfile
```
### Generate the doxygen file
```shell
podman run --rm -v "$(pwd):/data:Z" doxygen_py3.13 doxygen ./doc/Doxyfile
```

### open the document with browser
The doxygen file will be a 'html' file
``` shell
firefox ./doc/html/index.html
# or
google-chrome ./doc/html/index.html
# or
gio open ./doc/html/index.html
# or any tool you want 
```