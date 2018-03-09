# FROM ubuntu:16.04
FROM python:2.7-wheezy
FROM python:3
RUN apt-get update && apt-get install -y

# Set the working directory to /app
WORKDIR /usr/src/api_swagger

# Copy the current directory contents into the container at /app
COPY . /usr/src/api_swagger

# Install any needed packages specified in requirements.txt
RUN pip3 install  -r requirements.txt

EXPOSE 8090

#CMD ["./script.sh"]
