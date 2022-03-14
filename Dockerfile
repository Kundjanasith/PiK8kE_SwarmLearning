FROM tensorflow/tensorflow

EXPOSE 19191

COPY . .

WORKDIR ./learning/