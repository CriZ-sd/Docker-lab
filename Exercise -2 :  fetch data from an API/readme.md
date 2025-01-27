# Exercise -2 : fetch data from an API
create a container that runs a python app with request library to fetch data from an API

* create a folder named fetch_data_app and go to this folder
```
mkdir fetch_data_app
cd fetch_data_app
```
* copy the app.py python file
```
nano app.py
# paste the python script
ctrl +x
y
```
app.py : 
```
import requests

# Make a GET request to a public API
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Check if the request was successful
if response.status_code == 200:
    post = response.json()
    print("Post fetched from API:")
    print(f"Title: {post['title']}")
    print(f"Body: {post['body']}")
else:
    print("Failed to fetch post from API")
```
* create a Dockerfile
  > the Dockerfile includes a step-by-step guide of how to create the container
```
nano Dockerfile
# write the commands (steps)
ctrl +x
y
```
Dockerfile :
```
# Use the official Python image for Raspberry Pi (ARM architecture)
FROM arm32v7/python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY app.py /app/

# Install the requests library
RUN pip install requests

# Run the Python script when the container starts
CMD ["python", "app.py"]
```

* Build the Docker image
```
docker build -t rpi-python-requests-app .
```
* see all the available images
```
docker images
```
* run the docker container
```
docker run --rm rpi-python-requests-app
```
> --rm: Automatically removes the container after it finishes running.
* see the running docker containers
```
docker ps
```
