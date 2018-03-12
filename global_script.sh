#docker run --name=<container-name> -d <mongo-image> 
#docker run -t -d <api-image> 
#docker run --net=mynet1  --ip 10.118.225.196 -p 9089:9089 -itd blandry

# User Must Start In ./Falsy container
apiid=api7 #set api image name
mongoid=mongodb7 # set mongo image name

cd api/
docker build -t $apiid .

cd ..
cd mongodb/
docker build -t $mongoid .

docker run -t -d $apiid
docker run -d $mongoid

container_mongo=`docker ps | awk '{i++}i==2{print $1; exit}'`
container_api=`docker ps | awk '{i++}i==3{print $1; exit}'`

apt install jq #TODO: add the requirements.txt

### How to pass newMongoIP variable inside container and for sed to access it?
newMongoIP=`docker inspect $container_mongo | jq '.[].NetworkSettings.Networks.bridge.IPAddress'`

docker exec -it $container_api bash
sed -i "s/mongoIP/$newMongoIP/g" demo.py

apiIP=`awk 'END{print $1}' /etc/hosts`
gunicorn -b $apiIP:8090 main:api --reload -w 1 --threads 1