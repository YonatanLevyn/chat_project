from django.urls import path
from . import views

urlpatterns = [
    path("chat/", views.chat, name="chat"),
]
from django.conf import settings
from django.conf.urls.static import static



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
