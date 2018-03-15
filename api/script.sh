#!/bin/bash
#apiIP=`awk 'END{print $1}' /etc/hosts`

#python test_python.py
python demo.py
gunicorn -b $api:8090 main:api --reload -w 1 --threads 1
