FROM resin/raspberrypi3-python:2.7

# use apt-get if you need to install dependencies,
RUN apt-get update && apt-get install -yq \
	python-smbus \
   	curl && \
   	apt-get clean && rm -rf /var/lib/apt/lists/*

# Set our working directory
WORKDIR /usr/src/app

# Copy requirements.txt first for better cache on later pushes
COPY ./requirements.txt /requirements.txt

# pip install python deps from requirements.txt on the resin.io build server
RUN pip install -r /requirements.txt
COPY ./autohat_install.sh install.sh
RUN ./install.sh -y

# This will copy all files in our root to the working  directory in the container
COPY . ./

# switch on systemd init system in container
ENV INITSYSTEM on

# main.py will run when container starts up on the device
CMD modprobe i2c-dev && python -u src/main.py