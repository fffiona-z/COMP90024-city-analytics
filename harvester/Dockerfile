FROM python:3.7

WORKDIR ./data_harvester

ADD . .

RUN pip install -r requirement.txt

CMD ["python3", "./data_harvester/run.py"]

