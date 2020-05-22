FROM python:3.7

WORKDIR ./harvester

ADD . .

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]

CMD ["python3", "./run.py"]

