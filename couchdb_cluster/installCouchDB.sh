#!/bin/sh

curl -L https://couchdb.apache.org/repo/bintray-pubkey.asc | sudo apt-key add -

echo "deb https://apache.bintray.com/couchdb-deb bionic main" | sudo tee -a /etc/apt/sources.list

sudo apt update

sudo apt install couchdb

