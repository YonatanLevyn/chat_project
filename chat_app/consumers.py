"""
This module contains a WebSocket consumer (ChatConsumer) that handles chat communication
in a Django Channels application. It manages user connections, receives messages from
connected clients, and broadcasts messages to all connected clients in the chat room.

ChatConsumer extends the AsyncWebsocketConsumer class, which is an asynchronous WebSocket
consumer that provides several methods for managing connections, receiving messages,
and sending messages back to the clients.
"""

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Retrieve the room name from the URL route parameter
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # The group associated with that chat room
        self.room_group_name = f"chat_{self.room_name}"

        # Add this WebSocket connection to the chat group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Remove this WebSocket connection from the chat group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive a message from the WebSocket and process it
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

        # Send the message to the chat group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": username
            }
        )

    async def chat_message(self, event):
        # Receive a message from the chat group and send it to the WebSocket
        message = event["message"]
        username = event["username"]

        await self.send(text_data=json.dumps({
            "message": message,
            "username": username
        }))
