from django.shortcuts import render, get_object_or_404

def entry(request):
    return render(request, "chat_app/entry.html")

def chat_room(request):
    # Retrieve the username and roomname from the request's GET parameters
    room_name = request.GET.get("room_name", "")
    username = request.GET.get("username", "")

    #If the username or roomname is not provided or empty, render the entry page
    if room_name == "" or username == "":
        return render(request, "chat_app/entry.html")
    
    # Create or retrieve the chat room
    from .models import ChatRoom
    chat_room, created = ChatRoom.objects.get_or_create(name=room_name)

    return render(request, "chat_app/chat_room.html", {"room_name": room_name, "username": username, "chat_room": chat_room})





