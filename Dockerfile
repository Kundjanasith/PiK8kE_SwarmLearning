# FROM --platform=linux/arm64/v8 tensorflow/tensorflow
FROM tensorflow/tensorflow

RUN apt-get upgrade
RUN apt-get update
RUN apt-get -y install apt-utils
RUN apt-get -y install iputils-ping
RUN apt-get -y install telnet
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN python3 -m pip install tqdm
RUN python3 -m pip install keras
RUN apt-get -y install openssh-client
RUN apt-get -y install nano
RUN apt-get -y install ftp
RUN apt-get -y install screen
RUN apt-get -y install git

EXPOSE 19190
EXPOSE 19191
EXPOSE 19192

COPY . .

CMD ["bin/bash"]