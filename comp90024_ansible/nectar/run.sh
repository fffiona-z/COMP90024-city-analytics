#!/bin/bash

# apply the instances, render the templates
. ./openrc.sh; ansible-playbook --ask-become-pass apply_instance.yaml

# setup couchdb cluster on database servers
ansible-playbook -i inventory.ini -u ubuntu --key-file=./Group58 couchdb_cluster_setup.yml
