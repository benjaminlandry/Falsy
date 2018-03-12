#!/bin/bash
export MONGOIP=`docker ps | awk '{i++}i==2{print $1; exit}'`