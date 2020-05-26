#!/bin/sh

sudo apt install python3-pip

pip3 install -r requirements.txt

nohup python3 -u ./data_harvester/run1.py > output1 2>&1 &

echo 'start runing run1.py'

