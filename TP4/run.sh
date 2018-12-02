apt-get install -y mongodb
service mongodb start
pip3 install -r application/requirements.txt
python3 application/app.py
