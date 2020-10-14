FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04

LABEL maintainer = "alsurj <alvin.surjana@uni-due.de>"

RUN apt-get update --fix-missing && \
    apt-get install -y \
    apt-utils \
    build-essential \
	bzip2 \
    curl \
    ca-certificates \
    wget \
    git \
    vim \
    libssl-dev \
	libgl1-mesa-glx\
	libsm6 \
	libxrender1 \
	libfontconfig1 \
	libpython3.7-dev \
	libopenblas-dev\
    software-properties-common \
    unzip \
    unrar \
	wget \
    openssh-server \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# create a non-root user
ARG username=SRS
ARG uid=1000
ARG gid=100
ENV USER $username
ENV UID $uid
ENV GID $gid
ENV HOME /home/$USER

RUN adduser --disabled-password \
    --gecos "Non-root user" \
    --uid $UID \
    --gid $GID \
    --home $HOME \
    $USER

COPY environment.yml requirements.txt /tmp/
RUN chown $UID:$GID /tmp/environment.yml /tmp/requirements.txt

COPY postBuild /usr/local/bin/postBuild.sh
RUN chown $UID:$GID /usr/local/bin/postBuild.sh && \
    chmod u+x /usr/local/bin/postBuild.sh

COPY entrypoint.sh /usr/local/bin/
RUN chown $UID:$GID /usr/local/bin/entrypoint.sh && \
    chmod u+x /usr/local/bin/entrypoint.sh
	
USER $USER

RUN mkdir /var/run/sshd
RUN echo '$USER:test' | chpasswd
RUN sed -i 's/#*PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd

ENV NOTVISIBLE="in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
