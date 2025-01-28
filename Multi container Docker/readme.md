# Multi container management using docker compose 
## Learn how to use docker compose for multiple linking containers management 

* docker compose  is used to manage multiple containers at once 

* to use docker compose we need a yaml file to orchestrate the process 

* see if docker compose is downloaded
```
docker compose
```
* create an app dir
```
mkdir ~/docker-compose-app
cd ~/docker-compose-app
```
* create a yaml file that creates 2 containers and echo a message from each one
```
version: '3'

services:
  alpine1:
    image: alpine:latest
    command: sh -c "echo 'Hello from container 1!' && sleep 30"
    
  alpine2:
    image: alpine:latest
    command: sh -c "echo 'Hello from container 2!' && sleep 30"
  
```

* run the  containers
```
docker compose up
```  
* stop the containers and clean up (remove them)
```
docker compose down
```
* check for running containers
```
docker compose ps 
```
