FROM --platform=linux/amd64 tensorflow/tensorflow

EXPOSE 19191

COPY . .

WORKDIR ./learning/