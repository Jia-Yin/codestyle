# CodeStyle

## Test
```bash
docker build -t codestyle .
docker run -it --rm -v "$PWD":/home/root/app/vera codestyle bash
# cd vera
# ./vera++ -R L001 tests/L001.cpp
```