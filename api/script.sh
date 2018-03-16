#!/bin/bash
#apiIP=`awk 'END{print $1}' /etc/hosts`

#python demo.py
corsEnabled=True
gunicorn -b $api:8090 main:api --reload -w 1 --threads 1
