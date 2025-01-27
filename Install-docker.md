# Docker installation rpi 

* Check if already installed
```
docker --version 
```

* update your system
```
sudo apt-get update 
```

* install docker 
```
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl gnupg lsb-release
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

* check again if it is installed
```
docker --version
```

* add your user to the docker group → use docker without “sudo”
```
sudo  usermod   -aG   docker   $USER

ctrl+d (dis-connect and re-connect) 
```

* run hello-world example
```
docker run hello-world
```
* check if docker is loaded and enabled
```
sudo systemctl status docker
```

