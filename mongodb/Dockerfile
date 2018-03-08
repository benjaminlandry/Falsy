FROM mongo:3.0-wheezy
RUN apt-get update && apt-get install -y

WORKDIR /usr/src/mongodb

COPY . /usr/src/mongodb

#CMD ['./script.sh']

#RUN bash 'export ip=`awk 'END{print $1}' /etc/hosts`'
ENV ip="bash 'export ip=`awk 'END{print $1}' /etc/hosts`'"

EXPOSE 27017

#https://hub.docker.com/_/mongo/