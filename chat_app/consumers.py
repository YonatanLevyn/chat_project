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
from channels.db import database_sync_to_async

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

        # Save the message to the database
        user = await self.get_user(username)
        chat_room = await self.get_chat_room(self.room_name)

        from .models import ChatRoom, Message
        if user and chat_room:
            await self.save_message(chat_room, user, message)


    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]

        await self.send(text_data=json.dumps({
            "message": message,
            "username": username
        }))


    @database_sync_to_async
    def get_user(self, username):
        from django.contrib.auth.models import User
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    @database_sync_to_async
    def get_chat_room(self, room_name):
        from .models import ChatRoom
        try:
            return ChatRoom.objects.get(name=room_name)
        except ChatRoom.DoesNotExist:
            return None

    @database_sync_to_async
    def save_message(self, chat_room, user, message):
        from .models import Message
        Message.objects.create(chat_room=chat_room, user=user, content=message)
