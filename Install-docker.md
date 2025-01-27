# Docker installation rpi 

* Check if already installed
```
docker --version 
sudo docker --version
```

* update your system
```
sudo apt-get update 
```

* install docker 
```
curl  -fsSL   https://get.docker.com  -o get-docker.sh

sudo   sh   get-docker.sh
```

* add your user to the docker group → use docker without “sudo”
```
sudo  usermod   -aG   docker   $USER
```
* check again if it is installed
```
docker --version
```
* run hello-world example
```
docker run hello-world
```
* check if docker is loaded and enabled
```
sudo systemctl status docker
```

