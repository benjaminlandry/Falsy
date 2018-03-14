#docker run --name=<container-name> -d <mongo-image> 
#docker run -t -d <api-image> 
#docker run --net=mynet1  --ip 10.118.225.196 -p 9089:9089 -itd blandry

# User Must Start In ./Falsy container

#docker rmi -f $(docker images)
docker rm -f $(docker ps -a -q)
echo y | docker network rm my-network
echo y | docker network prune

#sleep(5)

apiid=api1 #set api image name
mongoid=mongodb1 # set mongo image name

cd api/
docker build -t $apiid .

cd ..
cd mongodb/
docker build -t $mongoid .

#set network
docker network create --driver=bridge my-network
docker run -t -d --net=my-network --name $apiid $apiid
docker run -t -d --net=my-network --name $mongoid $mongoid

#container_mongo=`docker ps | awk '{i++}i==2{print $1; exit}'`
#container_api=`docker ps | awk '{i++}i==3{print $1; exit}'`

#apt install jq

### How to pass newMongoIP variable inside container and for sed to access it?
#newMongoIP=`docker inspect $mongoid | jq '.[].NetworkSettings.Networks.bridge.IPAddress'`
#sudo echo $mongoid $newMongoIP >> /etc/resolv.conf

# docker exec -it $apiid bash
# sed -i "s/mongoIP/$mongodb6/g" demo.py

#apiIP=`awk 'END{print $1}' /etc/hosts`
#sudo echo $apiid $apiIP >> /etc/resolv.conf
#cd ..
#cd api


sh test_script.sh
#python test_python.py

#gunicorn -b $api5:8090 main:api --reload -w 1 --threads 1