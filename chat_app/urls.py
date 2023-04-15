from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Define the URL patterns for the app
urlpatterns = [
    path("chat/", views.chat, name="chat"),
]

# If in DEBUG mode, serve static files directly
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
