from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View

from messegeapp.forms import MessageForm
from messegeapp.models import Chat



class DialogView(View):

    def get(self, request):
        chats = Chat.objects.filter(members__in=[request.user.id])
        return render(request, 'messageapp/dialog.html', {'user_profiler': request.user, 'chats': chats})


class MessageView(View):
    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_read=False).exclude(author=request.user).update(is_read=True)
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None
        content = {
            'user_profile': request.user,
            'chat': chat,
            'form': MessageForm()
        }
        return render(request, 'messageapp/messages.html', context=content)

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('messegeapp:messages', kwargs={'chat_id': chat_id}))


class CreateDialogView(View):
    def get(self, request, user_id):
        chats = Chat.objects.filter(members__in=[request.user.id, user_id], type=Chat.DIALOG).annotate(
            c=Count('members')).filter(c=2)
        if chats.count() == 0:
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        return redirect(reverse('messegeapp:messages', kwargs={'chat_id': chat.id}))
