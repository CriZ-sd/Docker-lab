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

* find the web server online on : http://<your-raspberry-pi-ip>:8080 

## Check out the python code for nginx web server
