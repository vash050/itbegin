from django.shortcuts import render


# def chat(request):
#     return render(request, 'chatapp/chat.html')
from chatapp.models import RoomChat, MessageChat


def room(request, room_name):
    chat, b = RoomChat.objects.get_or_create(group_id=room_name)
    all_message = MessageChat.objects.filter(group=chat)
    context = {
        'room_name': room_name,
        'all_message': all_message
    }
    return render(request, 'chatapp/room.html', context=context)
