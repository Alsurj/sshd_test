FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04
LABEL maintainer=""

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

SHELL [ "//bin/bash", "--login", "-c" ]

WORKDIR /app

RUN apt-get update

RUN apt-get install -y\
      build-essential \
      software-properties-common \
      apt-utils \
      ca-certificates \
      wget \
      git \
      vim \
      libssl-dev \
      curl \
      unzip \
      unrar \
      libsm6 \
      libxrender1 \
      libfontconfig1 \
      libpython3.7-dev \
      libopenblas-dev \
   && rm -rf /var/lib/apt/lists/*

RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y


#Install conda

RUN wget --quiet \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh 

RUN conda --version

RUN conda create -n py3-mink python=3.7
RUN conda activate py3-mink
RUN conda install numpy mkl-include pytorch cudatoolkit=10.2 -c pytorch

RUN git clone https://github.com/NVIDIA/MinkowskiEngine.git \
	&& cd MinkowskiEngine \
	&& python setup.py install --blas=openblas









#RUN apt-get install -y libsm6 libxrender1 libfontconfig1 libpython3.7-dev libopenblas-dev


#RUN python3.7 -m pip install numpy \
# && python3.7 -m pip install scipy \
# && python3.7 -m pip install cython \
# && python3.7 -m pip install scikit-image \
# && python3.7 -m pip install sklearn \
# && python3.7 -m pip install opencv-python==4.1.1.26 \
# && python3.7 -m pip install torchvision==0.6.1 \
# && python3.7 -m pip install torch==1.5.1 
# && python3.7 -m pip install git+https://github.com/NVIDIA/MinkowskiEngine.git@v0.5

#ENV CUDA_HOME='/usr/local/cuda-10.2'

#RUN git clone https://github.com/NVIDIA/MinkowskiEngine.git@v0.5 \
# && cd MinkowskiEngine \
# && python3.7 setup.py install

#RUN python3.7 -m pip install git+https://github.com/NVIDIA/MinkowskiEngine.git@v0.5 \
#                           --install-option="--force_cuda" \
#                           --install-option="--cuda_home='/usr/local/cuda-10.2'" \ 
#                           --install-option="--blas=openblas"

#ADD . /FCGF
#RUN python3.7 -m pip install -r FCGF/requirements.txt


#EXPOSE 8888
#ARG USER_NAME
#ARG USER_ID
#RUN adduser --uid ${USER_ID} --gecos '' ${USER_NAME}
#RUN adduser ${USER_NAME} sudo
#RUN passwd -de ${USER_NAME}

CMD ["//bin/bash"]
