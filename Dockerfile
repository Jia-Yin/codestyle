FROM golang:1.12

EXPOSE 8080/tcp
ENV PORT 8080

RUN mkdir -p /home/root/app
WORKDIR /home/root/app
COPY . /home/root/app

RUN apt update && apt install tcl -y && apt install python-dev -y
RUN apt install ca-certificates libgnutls30 -y
ENV GO111MODULE=on
ENV GOPATH=/go
RUN go get github.com/gin-gonic/gin@v1.7.0
RUN go build *.go
COPY checkstyle /home/root/app/checkstyle
CMD ["/home/root/app/checkstyle"]
