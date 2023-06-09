# Chat App with Django

A simple real-time chat application built using Django, WebSockets, Daphne, and Redis. This project serves as a base application for any project that requires a chat feature. It provides a simple solution for real-time chat functionality.

## Getting Started with Docker

To run the chat application using Docker, follow these steps:

1. Clone the GitHub repository to your local machine:
```
git clone https://github.com/YonatanLevyn/chat_project.git
```

2. Navigate to the project directory:
```
cd chat_project
```

3. Build and run the Docker containers:
```
docker-compose up --build
```

4. Once the containers are up and running, open a web browser and navigate to `http://localhost:8000` to access the chat application.

5. To stop the containers and remove the network and volumes defined in the `docker-compose.yml` file, run the following command in the terminal:
```
docker-compose down
```


![Screenshot from 2023-06-08 02-34-35](https://github.com/YonatanLevyn/chat_project/assets/93859114/fd2c66ec-6284-4159-8cf5-d2538ea358f9)

![Screenshot from 2023-06-08 02-33-13](https://github.com/YonatanLevyn/chat_project/assets/93859114/d230618e-b58f-4a27-94b0-e8e55d8e5288)

## Upcoming Improvements
Looking ahead, I plan on implementing WebSocket Secure (WSS) using HAproxy. This will make the chat application more robust and ready-to-use for other projects.
