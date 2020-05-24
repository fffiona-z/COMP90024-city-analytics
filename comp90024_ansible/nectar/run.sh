#!/bin/bash

# apply the instances, render the templates
. ./openrc.sh; ansible-playbook --ask-become-pass apply-instance.yml

# setup couchdb cluster on database servers
ansible-playbook -i inventory.ini -u ubuntu --key-file=./Group58 couchdb-cluster-setup.yml