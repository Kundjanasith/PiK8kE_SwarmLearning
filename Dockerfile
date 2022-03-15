# FROM --platform=linux/arm64/v8 tensorflow/tensorflow
FROM ubuntu

RUN apt-get update
RUN apt-get -y install iputils-ping

EXPOSE 19190, 19191

COPY . .

