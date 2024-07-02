FROM --platform=linux/amd64 python:2.7

# Install dependencies

ARG USER_ID=1005
ARG GROUP_ID=1006
ARG USERNAME=nao
RUN groupadd --gid $GROUP_ID $USERNAME \
	&& useradd --uid $USER_ID --gid $GROUP_ID -m $USERNAME

RUN apt-get update && \
	apt-get install -y \
	python-pip \
	iproute2 \
	telnet \
	iputils-ping \
	wget\
	curl\
	build-essential\
	gcc \
	cmake \
	unzip \
	libenchant1c2a \
	libavformat-dev \
	libavcodec-dev \
	libavfilter-dev \
	libswscale-dev \
	libjpeg-dev \
	libpng-dev \
	libtiff-dev \
	zlib1g-dev \
	libopenexr-dev \
	libxine2-dev \
	libeigen3-dev \
	libtbb-dev && \
	rm -rf /var/lib/apt/lists/*

RUN pip install numpy paramiko

WORKDIR /naoqi

# Copy the NAOqi for Python SDK
COPY  naoqi-amd64-2.1.4.13.tar.bz2 .
RUN  tar jxfv naoqi-amd64-2.1.4.13.tar.bz2

# Set the path to the SDK
EXPOSE 9559
USER nao
CMD /naoqi/naoqi-sdk-2.1.4.13-linux64/naoqi

