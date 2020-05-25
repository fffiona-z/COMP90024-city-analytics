#!/bin/sh

sudo apt install python-pip

pip install -r requirements.txt

nohup python app.py >/home/ubuntu/output 2>&1 &
