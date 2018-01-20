FROM resin/raspberrypi3-python:2.7

# use apt-get if you need to install dependencies,
RUN apt-get update && apt-get install -yq \
	python-smbus \
	dnsmasq \
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

ADD wifi-connect-linux-armv7hf.tar.gz .
RUN mv wifi-connect /usr/bin/wifi-connect
# This will copy all files in our root to the working  directory in the container
COPY . ./

ENV DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket

# main.py will run when container starts up on the device
CMD modprobe i2c-dev && python -u src/main.py