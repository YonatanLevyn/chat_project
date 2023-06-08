# Chat App

This is a simple real-time chat application built using Django, WebSockets, Daphne, and Redis.

## Features

- Real-time chat
- User authentication
- Easy-to-use interface

## Technologies

- Django: A high-level Python web framework for building web applications
- WebSockets: A communication protocol for real-time data exchange between clients and servers
- Daphne: An ASGI server for running Django applications, enabling WebSocket support
- Redis: An in-memory data store used as a message broker for Django Channels


## Getting Started with Docker

To run the chat application using Docker, follow these steps:

1. Make sure you have Docker and Docker Compose installed on your system. If not, refer to the [official Docker documentation](https://docs.docker.com/engine/install/) for installation instructions.

2. Clone the GitHub repository to your local machine:
```
git clone https://github.com/YonatanLevyn/chat_project.git
```

3. Navigate to the project directory:
```
cd chat_project
```

4. Build and run the Docker containers:
```
docker-compose up --build
```

5. Once the containers are up and running, open a web browser and navigate to `http://localhost:8000` to access the chat application.

6. To stop the containers and remove the network and volumes defined in the `docker-compose.yml` file, run the following command in the terminal:
```
docker-compose down
```


![Screenshot from 2023-06-08 02-34-35](https://github.com/YonatanLevyn/chat_project/assets/93859114/fd2c66ec-6284-4159-8cf5-d2538ea358f9)

![Screenshot from 2023-06-08 02-33-13](https://github.com/YonatanLevyn/chat_project/assets/93859114/d230618e-b58f-4a27-94b0-e8e55d8e5288)

