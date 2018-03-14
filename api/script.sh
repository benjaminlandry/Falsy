#!/bin/bash
#apiIP=`awk 'END{print $1}' /etc/hosts`
gunicorn -b $MONGODB_HOST:8090 main:api --reload -w 1 --threads 1