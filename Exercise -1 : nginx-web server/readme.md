# Exercise -1 : nginx-web server
Use nginx container to create a webserver form your local machine 

## Docker implementation 
* pull nginx docker image
```
docker pull nginx
```

 * run an nginx container
```
docker run -d -p 8080:80 --name my-nginx nginx
```
> -d : detatched mode , -p : Map port 8080 on your Pi to port 80 inside the container

* find the web server online on : http://<your-raspberry-pi-ip>:8080 

* check for running containers
```
docker ps
```
> copy the container id 

* stop the running contrainer
```
docker stop "container_id"
```
* see all docker containers running and stopped
```
docker ps --all
```

* see all downloaded images
```
docker images
```

## Check out the python code for nginx web server

