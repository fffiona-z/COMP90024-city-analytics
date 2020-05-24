#!/bin/sh

curl -X POST -H "Content-Type: application/json" http://admin:12345@127.0.0.1:5984/_cluster_setup -d '{"action": "enable_cluster", "bind_address":"0.0.0.0", "username": "admin", "password":"12345", "port": 5984, "remote_node": "45.113.234.166", "remote_current_user": "admin", "remote_current_password": "12345" }'

curl -X POST -H "Content-Type: application/json" http://admin:12345@127.0.0.1:5984/_cluster_setup -d '{"action": "add_node", "host":"45.113.234.166", "port": "5984", "username": "admin", "password":"12345"}'

curl -X POST -H "Content-Type: application/json" http://admin:12345@127.0.0.1:5984/_cluster_setup -d '{"action": "enable_cluster", "bind_address":"0.0.0.0", "username": "admin", "password":"12345", "port": 5984, "remote_node": "115.146.94.167", "remote_current_user": "admin", "remote_current_password": "12345" }'

curl -X POST -H "Content-Type: application/json" http://admin:12345@127.0.0.1:5984/_cluster_setup -d '{"action": "add_node", "host":"115.146.94.167", "port": "5984", "username": "admin", "password":"12345"}'

curl -X POST -H "Content-Type: application/json" http://admin:12345@127.0.0.1:5984/_cluster_setup -d '{"action": "finish_cluster"}'