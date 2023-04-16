
from django.shortcuts import render

def entry(request):
    return render(request, "chat_app/entry.html")

def chat_room(request):
    # Retrieve the username and roomname from the request's GET parameters
    room_name = request.GET.get("room_name", "")
    username = request.GET.get("username", "")

    #If the username or roomname is not provided or empty, render the entry page
    if room_name == "" or username == "":
        return render(request, "chat_app/entry.html")

    return render(request, "chat_app/chat_room.html", {"room_name": room_name, "username": username})
