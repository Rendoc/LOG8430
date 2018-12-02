#!/bin/bash

apt-get install -y python-pip && \
	apt-get install -y python2.7 && \
	apt-get install -y mongodb
service mongodb start
pip --no-cache-dir install pyspark
pip install -r application/requirements.txt
python2.7 application/app.py
