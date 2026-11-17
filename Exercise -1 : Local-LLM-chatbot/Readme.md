# 🤖 Build Your Own Local AI Chatbot with Docker

In this tutorial, we'll create our own **local LLM chatbot assistant** using Docker!

We'll use a lightweight, open-source language model called **Qwen2.5-0.5B-Instruct** and run it inside a Docker container using **llama.cpp**.


## Step 1: Create a Directory for the AI Model

First, create a directory to store the model files.

```bash
cd ~
mkdir -p ai-models
cd ai-models
```

## Step 2: Download the LLM Model

We'll use the quantized version of **Qwen2.5-0.5B-Instruct**, a lightweight language model suitable for running on CPUs.

Download the model weights:

```bash
curl -fL --retry 3 \
  -o qwen.gguf \
  https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q4_k_m.gguf
```

The model is approximately 491 MB.

Verify that the file was downloaded:

```bash
ls -lh qwen.gguf
```

## Step 3: Pull the Docker Image

We'll use a lightweight Docker image containing **llama.cpp**, an open-source LLM inference engine.

Pull the image from Docker Hub:

```bash
docker pull ghcr.io/ggml-org/llama.cpp:server
```

Docker Hub image:

https://hub.docker.com/r/samueltallet/alpine-llama-cpp-server

## Step 4: Run the AI Chatbot Container

Start the LLM server inside a Docker container:

```bash
docker run -d \
  --name ai-chatbot \
  --restart unless-stopped \
  -p 8080:8080 \
  -v "$HOME/ai-models:/models:ro" \
  ghcr.io/ggml-org/llama.cpp:server \
  -m /models/qwen.gguf \
  --host 0.0.0.0 \
  --port 8080 \
  -c 1024 \
  -t 2
```

### Understanding the Docker Command

| Option | Description |
|---|---|
| `-d` | Runs the container in the background |
| `--name ai-chatbot` | Assigns a name to the container |
| `-p 8080:8080` | Maps port 8080 of the container to port 8080 of the host |
| `-v "$HOME/ai-models:/models:ro"` | Mounts the model directory as read-only inside the container |
| `-m /models/qwen.gguf` | Specifies which LLM to load |
| `--host 0.0.0.0` | Allows the server to accept connections through the container's network interface |
| `--port 8080` | Specifies the server port |
| `-c 1024` | Sets the model context window to 1024 tokens |
| `-t 2` | Uses two CPU threads for inference |

## Step 5: Verify That the Container Is Running

List running containers:

```bash
docker ps
```

Check the logs:

```bash
docker logs ai-chatbot
```

The server may need some time to load the model.

## Step 6: Open the Chatbot in Your Browser

In Google Cloud Shell:

1. Click **Web Preview** in the Cloud Shell toolbar. (Port `8080`)
2. Once the server is ready, interact with your local AI chatbot using the llama.cpp web interface.

You can now ask your AI assistant questions directly from your browser!

## Step 6: Stop and Remove the Container

When you've finished experimenting, stop the container:

```bash
docker stop ai-chatbot
```

Remove it:

```bash
docker rm ai-chatbot
```

Verify that it has been removed:

```bash
docker ps -a
```

**Note:** Removing the container does not delete the downloaded model, because the model is stored on your host filesystem.

### Optional Cleanup

Remove the Docker image:

```bash
docker rmi samueltallet/alpine-llama-cpp-server:latest
```

Remove the downloaded model:

```bash
rm ~/ai-models/qwen.gguf
```

## What Did We Learn?

In this tutorial, we learned how to:

- Download and use an open-source LLM.
- Pull a Docker image from Docker Hub.
- Run an AI model inside a Docker container.
- Use Docker port mapping to access a service.
- Mount local files into containers using bind mounts.
- Interact with an LLM through a browser or REST API.
- Stop and remove Docker containers.

## Useful Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Hub – Alpine llama.cpp Server](https://hub.docker.com/r/samueltallet/alpine-llama-cpp-server)
- [Qwen2.5-0.5B-Instruct Model](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF)
- [llama.cpp GitHub Repository](https://github.com/ggml-org/llama.cpp)
- [Google Cloud Shell Documentation](https://cloud.google.com/shell/docs)

---

**Congratulations! 🎉**

You've successfully created your own local AI chatbot using Docker, an open-source language model, and Google Cloud Shell — without requiring a GPU or an external AI API.
