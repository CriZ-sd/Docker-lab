# Docker Commands Recap

## 1. Running Containers

| **Command**                                | **Description**                                      |
|--------------------------------------------|------------------------------------------------------|
| `docker run [OPTIONS] IMAGE [COMMAND]`     | Run a container from an image                       |
| `docker run -d -p HOST:CONTAINER IMAGE`    | Run a container in detached mode with port mapping  |
| `docker run -it IMAGE /bin/bash`           | Run a container interactively with a shell          |
| `docker ps`                                | List running containers                             |
| `docker ps -a`                             | List all containers (including stopped ones)        |
| `docker stop CONTAINER_NAME_OR_ID`         | Stop a running container                            |
| `docker start CONTAINER_NAME_OR_ID`        | Start a stopped container                           |
| `docker restart CONTAINER_NAME_OR_ID`      | Restart a running or stopped container              |
| `docker exec -it CONTAINER_NAME /bin/bash` | Execute a command or shell inside a running container |
| `docker logs CONTAINER_NAME_OR_ID`         | View the logs of a container                        |

---

## 2. Managing Containers

| **Command**                                | **Description**                                      |
|--------------------------------------------|------------------------------------------------------|
| `docker rm CONTAINER_NAME_OR_ID`           | Remove a stopped container                          |
| `docker rm -f CONTAINER_NAME_OR_ID`        | Force remove a running container                    |
| `docker inspect CONTAINER_NAME_OR_ID`      | View detailed information about a container         |
| `docker export CONTAINER_NAME > file.tar`  | Export a container’s filesystem to a tarball        |
| `docker import file.tar`                   | Import a container from a tarball                  |

---

## 3. Managing Images

| **Command**                                | **Description**                                      |
|--------------------------------------------|------------------------------------------------------|
| `docker images`                            | List all images stored locally                      |
| `docker rmi IMAGE_NAME_OR_ID`              | Remove an image                                     |
| `docker build -t IMAGE_NAME .`             | Build an image from a Dockerfile                   |
| `docker tag IMAGE_NAME NEW_TAG`            | Tag an image with a new name or version             |
| `docker pull IMAGE_NAME`                   | Pull an image from Docker Hub                      |
| `docker push IMAGE_NAME`                   | Push a local image to Docker Hub                   |
| `docker inspect IMAGE_NAME`                | View detailed information about an image           |

---

## 4. Docker Compose

| **Command**                                | **Description**                                      |
|--------------------------------------------|------------------------------------------------------|
| `docker compose up`                        | Start services defined in `docker-compose.yml`      |
| `docker compose up -d`                     | Start services in detached mode                    |
| `docker compose down`                      | Stop and remove containers defined in `docker-compose.yml` |
| `docker compose ps`                        | List containers managed by Docker Compose          |
| `docker compose logs`                      | View logs for containers managed by Compose         |
| `docker compose logs -f`                   | Follow real-time logs for services                 |
| `docker compose exec SERVICE COMMAND`      | Execute a command inside a running service container |
| `docker compose build`                     | Build or rebuild services                          |
| `docker-compose up --scale SERVICE=NUMBER` | Scale a service to the specified number of instances |

---

## 5. Docker Hub

| **Command**                                | **Description**                                      |
|--------------------------------------------|------------------------------------------------------|
| `docker login`                             | Log in to Docker Hub                                |
| `docker search IMAGE_NAME`                 | Search for an image on Docker Hub                  |
| `docker pull IMAGE_NAME`                   | Pull an image from Docker Hub                      |
| `docker push IMAGE_NAME`                   | Push a local image to Docker Hub                   |

---

## 6. Cleanup Commands

| **Command**                                | **Description**                                      |
|--------------------------------------------|------------------------------------------------------|
| `docker system prune`                      | Remove unused containers, networks, and images      |
| `docker system prune -a`                   | Remove all unused images (not just dangling ones)   |
| `docker volume prune`                      | Remove all unused volumes                          |
| `docker network prune`                     | Remove all unused networks                         |
