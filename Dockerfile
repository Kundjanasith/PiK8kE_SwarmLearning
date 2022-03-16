FROM ubuntu

RUN apt-get upgrade
RUN apt-get update
RUN apt-get -y install apt-utils
RUN apt-get -y install iputils-ping
RUN apt-get -y install telnet
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN python3 -m pip install tqdm
# RUN python3 -m pip install keras
#TF
RUN apt-get -y install gfortran
RUN apt-get -y install libhdf5-dev libc-ares-dev libeigen3-dev
RUN apt-get -y install libatlas-base-dev libopenblas-dev libblas-dev
RUN apt-get -y install openmpi-bin libopenmpi-dev
RUN apt-get -y install liblapack-dev cython
RUN python3 -m pip install keras_applications==1.0.8 --no-deps
RUN python3 -m pip install keras_preprocessing==1.1.0 --no-deps
RUN python3 -m pip install -U --user six wheel mock
RUN python3 -m pip install pybind11
RUN python3 -m pip install h5py==2.10.0
RUN python3 -m pip install --upgrade setuptools
RUN python3 -m pip install gdown
RUN gdown https://drive.google.com/uc?id=11mujzVaFqa7R1_lB7q0kVPW22Ol51MPg
RUN python3 -m pip install tensorflow-2.2.0-cp37-cp37m-linux_armv7l.whl wrapt --upgrade --ignore-installed

# RUN apt-get -y install openssh-client
# RUN apt-get -y install nano
# RUN apt-get -y install ftp
# RUN apt-get -y install screen
# RUN apt-get -y install git

# EXPOSE 19190
# EXPOSE 19191
# EXPOSE 19192

# COPY . .

# CMD ["bin/bash"]