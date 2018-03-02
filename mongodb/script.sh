#setting arguments
set mongo1 
arg1=$1

#docker build -t mongo3
#docker run --name mongo3 -d mongo

#systemctl docker restart
#docker rm $(docker ps -a -q)


#deleting docker images
# docker rmi -f $(docker images | grep api-proxy  awk '{print $3}')
# docker rmi -f $(docker images | grep api-proxy | grep v1 | awk '{print $3}')

