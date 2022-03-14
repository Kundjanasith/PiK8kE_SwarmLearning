FROM tensorflow/tensorflow

EXPOSE 19191

COPY . .

ENTRYPOINT ["./config.ini"]

WORKDIR ./learning/