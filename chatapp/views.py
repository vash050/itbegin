from django.shortcuts import render


def chat(request):
    return render(request, 'chatapp/chat.html')


def room(request, room_name):
    return render(request, 'chatapp/room.html', {'room_name': room_name})
