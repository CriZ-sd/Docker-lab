# Docker hub

* create an account on https://hub.docker.com/

## Using Docker hub to upload local image 
* log in locally
```
docker login -u "username"
```
> then enter your password

### Upload rpi-python-requests-app on docker hub
* tag the image
```
docker tag rpi-python-requests-app "username"/rpi-python-requests-app:v1
```
* push the image
```
docker push "username"/rpi-python-requests-app:v1
```
* check on your docker hub for the image
* delete the local image and the local folder and see the available images
```
docker rmi "username"/rpi-python-requests-app:v1
cd ~
rm -r fetch_data_app
docker images
```
* run again the image
```
docker run --rm  crizsd/rpi-python-requests-app:v1
```
* see the available images and remove the image 
```
docker images
docker rmi "username"/rpi-python-requests-app:v1
```
