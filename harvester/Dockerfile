FROM python:3.7

WORKDIR ./harvester

ADD . .

RUN pip install -r requirements.txt

CMD ["python3", "./data_harvester/run.py"]

