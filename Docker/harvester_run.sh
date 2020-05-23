#!/bin/sh
docker login -u fei0990
docker pull fei0990/comp90024_city_analysis:harvester
docker tag fei0990/comp90024_city_analysis:harvester data_harvester:latest
docker run --name harvester -d data_harvester
