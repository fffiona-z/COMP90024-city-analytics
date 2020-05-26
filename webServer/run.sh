#!/bin/sh

sudo apt install python-pip

pip install -r requirements.txt

nohup python app.py > output 2>&1 &

echo 'Server is running'
