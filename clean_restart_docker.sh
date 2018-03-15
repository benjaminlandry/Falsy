docker rm -f $(docker ps -a -q)
echo y | docker network rm my-network
echo y | docker network prune
docker rmi -f $(docker images)
docker volume rm $(docker volume ls -qf dangling=true)