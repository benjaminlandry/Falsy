#!/bin/sh
gunicorn -b 0.0.0.0:8089 main:api --reload -w 1 --threads 1