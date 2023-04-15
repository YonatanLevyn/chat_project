# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /code

# Install any needed packages specified in requirements.txt
COPY requirements.txt /code/
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install netcat
RUN apt-get update && apt-get install -y netcat

# Copy the current directory contents into the container at /code
COPY . /code/

# Add wait-for.sh script and make it executable
COPY wait-for.sh /code/
RUN chmod +x /code/wait-for.sh

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your app using Daphne
CMD ["daphne", "chat_project.asgi:application", "--bind", "0.0.0.0:8000", "-v", "2"]
