from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Define the URL patterns for the app
urlpatterns = [
    path("", views.entry, name="entry"),
    path("chat_room/", views.chat_room, name="chat_room"),
]

# If in DEBUG mode, serve static files directly
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
