docker rm -f $(docker ps -a )
echo y | docker network rm my-network
echo y | docker network prune
#first kill mongodb

docker-compose up