from django.urls import path

import chatapp.views as chatapp

app_name = 'chatapp'

urlpatterns = [
    # path('', chatapp.chat, name='chatapp'),
    path('<int:room_name>/', chatapp.room, name='room'),
]