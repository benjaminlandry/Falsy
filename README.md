Starting Mongo + Swagger:
docker start $(docker ps -a -q)
go to and open RoboMongo

In CMD:
gunicorn -b 0.0.0.0:8001 main:api --reload -w 1 --threads 1
In Web-browser:
http://0.0.0.0:8001/v1/ui/