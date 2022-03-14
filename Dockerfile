FROM tensorflow/tensorflow

COPY . .
WORKDIR ./learning/client/

RUN python3 train.py