#!/bin/sh
apiIP=`awk 'END{print $1}' /etc/hosts`
gunicorn -b $apiIP:8090 main:api --reload -w 1 --threads 1