FROM python:2.7-wheezy
FROM python:3
FROM benjaminlandry/swagger_falsy_libs:falsy_libs
RUN apt-get update && apt-get install -y 

#ENV MONGODB_HOST=10.0.1.1
# Set the working directory to /app

# Copy the current directory contents into the container at /app
WORKDIR /usr/src/api_swagger
COPY . /usr/src/api_swagger

EXPOSE 8090

CMD ['./usr/src/api_swagger/script.sh']