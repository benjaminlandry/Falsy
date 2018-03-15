FROM mongo:3.0-wheezy
RUN apt-get update && apt-get install -y

WORKDIR /usr/src/mongodb

COPY . /usr/src/mongodb

EXPOSE 27017

#https://hub.docker.com/_/mongo/

#bridge network | put container on same network | refer to them by container name