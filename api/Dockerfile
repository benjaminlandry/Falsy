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

ENV TCM_API_host = 0.0.0.0

EXPOSE 8089

CMD ["./script.sh"]
