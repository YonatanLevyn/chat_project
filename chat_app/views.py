from django.shortcuts import render

def chat(request):
    # Retrieve the username from the request's GET parameters
    username = request.GET.get("username", "")

    # If the username is not provided or empty, render the entry page
    if username == "":
        return render(request, "chat_app/entry.html")

    # If the username is provided, render the chat page and pass the username
    return render(request, "chat_app/chat.html", {"username": username})
