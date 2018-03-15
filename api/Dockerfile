FROM python:2.7-wheezy
FROM python:3
FROM benjaminlandry/swagger_falsy_libs:falsy_libs
RUN apt-get update && apt-get install -y

RUN \
  mkdir /api_swagger
COPY . /api_swagger
WORKDIR /api_swagger

EXPOSE 8090

CMD echo $MONGODB_HOST && \
exec ./script.sh

#ENV MONGODB_HOST=10.0.1.1