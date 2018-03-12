FROM mongo:3.0-wheezy
RUN apt-get update && apt-get install -y iputils-ping

WORKDIR /usr/src/mongodb

COPY . /usr/src/mongodb

#CMD ['./script.sh']
#RUN bash 'export ip=`awk 'END{print $1}' /etc/hosts`'
#ENV MONGOIP="bash 'export ip=`awk 'END{print $1}' /etc/hosts`'"
#ENV MONGOIP='1.2.3.4'

EXPOSE 27017

#https://hub.docker.com/_/mongo/

#bridge network | put container on same network | refer to them by container name