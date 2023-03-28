from django.shortcuts import render

def chat(request):
    username = request.GET.get("username", "")
    if username == "":
        return render(request, "chat_app/entry.html")
    return render(request, "chat_app/chat.html", {"username": username})
