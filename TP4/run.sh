#!/bin/bash

apt-get install -y python-pip
apt-get install -y mongodb
service mongodb start
pip install -r application/requirements.txt
python2.7 application/app.py
