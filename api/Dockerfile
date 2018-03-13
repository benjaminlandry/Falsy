# FROM ubuntu:16.04
FROM python:2.7-wheezy
FROM python:3
FROM benjaminlandry/swagger_falsy_libs:falsy_libs
RUN apt-get update && apt-get install -y iputils-ping

# Set the working directory to /app
WORKDIR /usr/src/api_swagger

# Copy the current directory contents into the container at /app
COPY . /usr/src/api_swagger

EXPOSE 8090

CMD ['./script.sh']