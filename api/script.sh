#!/bin/bash
#apiIP=`awk 'END{print $1}' /etc/hosts`
#gunicorn -b $api:8090 main:api --reload -w 1 --threads 1
python test_python.py
gunicorn -b $api:8090 main:api --reload -w 1 --threads 1
