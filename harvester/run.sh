#!/bin/sh

sudo apt install python-pip

pip install -r requirements.txt

nohup python ./data_harvester/run1.py >/home/ubuntu/output1 2>&1 &

echo 'start runing run1.py'

nohup python ./data_harvester/run2.py >/home/ubuntu/output2 2>&1 &

echo 'start runing run2.py'
