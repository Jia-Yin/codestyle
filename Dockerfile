FROM golang:1.12

EXPOSE 8080/tcp
ENV PORT 8080

RUN mkdir -p /home/root/app
WORKDIR /home/root/app
COPY vera++ /home/root/app/vera++
#COPY ./drunner ./runner

RUN apt update && apt install tcl -y && apt install python-dev -y

#CMD ["/home/root/app/app"]
