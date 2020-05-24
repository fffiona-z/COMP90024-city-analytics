#!bin/sh

sudo docker pull nginx
sudo docker run --name nginx -p 8080:80 -d nginx
sudo docker cp /home/ubuntu/COMP90024-city-analytics/nginx/nginx.conf nginx:/etc/nginx/nginx.conf
sudo docker restart nginx

