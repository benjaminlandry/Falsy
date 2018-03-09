#docker run --name=<container-name> -d <mongo-image> 
#docker run -t -d <api-image> 
#docker run --net=mynet1  --ip 10.118.225.196 -p 9089:9089 -itd blandry
#container_id1=`docker ps | awk '{print $1}' | head -2` #TODO: ensure passing variable works

# start in /Falsy
apiid=api2
mongoid=mongo2

cd api/
docker build -t $apiid .

cd ..
cd mongodb/
docker build -t $mongoid .

docker run -d $apiid
docker run -t -d $mongoid

container_id1=`docker ps | awk '{i++}i==2{print $1; exit}'`
container_id2=`docker ps | awk '{i++}i==3{print $1; exit}'`

docker exec -it $container_id1 bash
newMongoIP=`awk 'END{print $1}' /etc/hosts`
sed -i 's/mongoIP/$newMongoIP/g' demo.py

docker exec -it $container_id2 bash
apiIP=`awk 'END{print $1}' /etc/hosts`
gunicorn -b $apiIP:8090 main:api --reload -w 1 --threads 1