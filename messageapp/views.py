from django.db.models import Count
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.base import View
from rest_framework import generics

from messageapp.models import Dialog, Message
from messageapp.serializers import MessageSerializer


class DialogsApi(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        self.kwargs['user_id'] = request.user.id
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Message.objects.filter(dialog__members__in=[self.kwargs['user_id']])
        return queryset


class MessageCreateApi(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        self.kwargs['user_id'] = request.user.id
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Message.objects.filter(dialog__members__in=[self.kwargs['user_id']])
        return queryset


class CreateDialogView(View):
    def get(self, request, user_id):
        chats = Dialog.objects.filter(members__in=[request.user.id, user_id]).annotate(
            c=Count('members')).filter(c=2)
        if chats.count() == 0:
            chat = Dialog.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        return redirect(reverse('messageapp:dialog', kwargs={'dialog_id': chat.id}))
