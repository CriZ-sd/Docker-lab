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
