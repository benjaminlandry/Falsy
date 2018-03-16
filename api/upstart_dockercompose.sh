#echo 'y' |docker system prune
docker ps --all --quiet --filter="status=exited" | xargs --no-run-if-empty docker rm --volumes
docker volume rm -f $(docker volume ls --quiet --filter="dangling=true")
docker rmi api
docker build -t api .
docker-compose up