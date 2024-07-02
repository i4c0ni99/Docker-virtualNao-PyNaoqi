FROM --platform=linux/amd64 python:2.7

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
COPY  pynaoqi-python2.7-2.1.4.13-linux64.tar.gz .

RUN  tar zxfv pynaoqi-python2.7-2.1.4.13-linux64.tar.gz

# Copy the boost fix
# See https://community.ald.softbankrobotics.com/en/forum/import-issue-pynaoqi-214-ubuntu-7956
COPY boost/* ./pynaoqi-python2.7-2.1.4.13-linux64/

# Set the path to the SDK
ENV PYTHONPATH=${PYTHONPATH}:/naoqi/pynaoqi-python2.7-2.1.4.13-linux64
ENV LD_LIBRARY_PATH="/naoqi/pynaoqi-python2.7-2.1.4.13-linux64:$LD_LIBRARY_PATH"

#WORKDIR /app
#CMD bash
