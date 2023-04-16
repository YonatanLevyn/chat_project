"""
ASGI config for chat_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chat_app import consumers

# Set the default Django settings module for the ASGI application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat_project.settings")

# Get the default Django ASGI application
django_asgi_app = get_asgi_application()

# Defining the WebSocket URL routing directly in the ASGI configuration file
websocket_urlpatterns = [
    path("ws/chat/<str:room_name>/", consumers.ChatConsumer.as_asgi()),
]

# Configure the ASGI application to use Django for HTTP and WebSocket requests
application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns
            )
        ),
    }
)


