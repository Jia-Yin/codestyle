# CodeStyle

## Test
```bash
docker build -t codestyle .

# Dev
docker run -it --rm -p 8080:8080 -v "$PWD":/home/root/app/dev codestyle bash
# cd dev
# go run *.go

# Final
docker run --rm -p 8080:8080 codestyle
```