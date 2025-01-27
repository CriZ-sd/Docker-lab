# Docker-lab


## What is docker?
* software platform that allows you to build, test, and deploy applications quickly
* packages software into standardized units called containers →  everything the software needs to run (libraries, system tools, code, etc.)
* quickly deploy and scale applications into any environment and know your code will run
## Why docker ?
* Less is more → Simplicity in deployment : bundle application into a container, and it will run the same way on any machine that has Docker installed
* Isolation : each application isolated inside a container → if one application crashes the other not affected
* Resource Efficiency :  Containers share the system's resources (like memory and CPU) but stay isolated from each other → lightweight  and faster compared  to VMs for example
* Consistency :  runs the same whether it's on local machine, on a server, or in the cloud → NO compatibility issues
* Portability :  easily move containers between different environments  

## Docker key components 
* Docker Engine : running and managing containers
** Docker Daemon : background → manage Docker objects like images and containers
** Docker CLI 
* Docker Images:  “template” or “blueprint” for creating containers
** code, libraries,system tools, etc. 
** Layers: Images  → built in layers : each  represents a change 
* Docker Containers :  a running instance of a Docker image → it behaves like an independent, small virtual machine
* Dockerfile: script-like file that contains instructions to build a Docker image
* Docker Networks : allow containers to communicate with each other or with external systems.
* Docker Volumes : used to persist data outside of containers (Containers →  stateless by design → when a container is stopped or deleted, all the data inside it → lost )


Auth elab - Docker 
