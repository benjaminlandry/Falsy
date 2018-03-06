FROM mongo:3.0-wheezy
FROM python:2.7-wheezy
RUN apt-get update && apt-get install -y

WORKDIR /usr/src/mongodb

COPY . /usr/src/mongodb

# Install any needed packages specified in requirements.txt
#RUN pip install  -r requirements.txt

ENV TCM_DB_host = 0.0.0.0

EXPOSE 27017

#https://hub.docker.com/_/mongo/

#Running Dockerfile and Image
#docker build -t mongo1
#docker run --name=mongo1 mongo1