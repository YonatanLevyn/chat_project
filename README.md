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


## Contributing

Please feel free to contribute to this project by submitting issues, pull requests, or providing feedback.

For more information on each technology used, refer to their official documentation:

- [Django](https://docs.djangoproject.com/en/stable/)
- [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
- [Daphne](https://github.com/django/daphne)
- [Redis](https://redis.io/documentation)

