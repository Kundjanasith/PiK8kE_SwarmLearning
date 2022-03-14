FROM --platform=linux/arm64/v8 tensorflow/tensorflow

EXPOSE 19191

COPY . .

WORKDIR ./learning/