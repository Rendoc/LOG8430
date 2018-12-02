#!/bin/bash

apt-get install -y python-pip && \
	apt-get install -y python2.7 && \
	apt-get install -y mongodb && \
	apt-get install -y openjdk-8-jre-headless
service mongodb start
pip --no-cache-dir install -r application/requirements.txt
python2.7 application/app.py
