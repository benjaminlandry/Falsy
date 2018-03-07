#!/bin/sh
ip=`awk 'END{print $1}' /etc/hosts`
gunicorn -b $ip:8090 main:api --reload -w 1 --threads 1