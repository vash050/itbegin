from django.db.models import Count
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.base import View

from messageapp.forms import MessageForm
from messageapp.models import Dialog


class DialogsView(View):
    def get(self, request, dialog_id=0):
        chats = Dialog.objects.filter(members__in=[request.user.id])
        try:
            chat = Dialog.objects.get(id=dialog_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_read=False).exclude(author=request.user).update(is_read=True)
            else:
                chat = None
        except Dialog.DoesNotExist:
            chat = None

        context = {
            'user_profile': request.user,
            'chats': chats,
            'chat': chat,
            'form': MessageForm()
        }
        return render(request, 'messageapp/dialog_list.html', context=context)

    def post(self, request):
        form = MessageForm(data=request.POST)
        print(self.kwargs['dialog_id'])
        chat = Dialog.objects.get(id=self.kwargs['dialog_id'])
        if form.is_valid():
            message = form.save(commit=False)
            message.dialog = chat
            message.author = request.user
            message.save()
        return redirect(reverse('messageapp:dialog', kwargs={'dialog_id': self.kwargs['dialog_id']}))


# class MessagesView(View):
#     def get(self, request, dialog_id):
#
#         try:
#             chat = Dialog.objects.get(id=dialog_id)
#             if request.user in chat.members.all():
#                 chat.message_set.filter(is_read=False).exclude(author=request.user).update(is_read=True)
#             else:
#                 chat = None
#         except Dialog.DoesNotExist:
#             chat = None
#
#         return render(
#             request,
#             'messageapp/messages.html',
#             {
#                 'user_profile': request.user,
#                 'chat': chat,
#                 'form': MessageForm()
#             }
#         )
#
#     def post(self, request, dialog_id):
#         form = MessageForm(data=request.POST)
#         chat = Dialog.objects.get(id=dialog_id)
#         if form.is_valid():
#             message = form.save(commit=False)
#             message.dialog = chat
#             message.author = request.user
#             message.save()
#         return redirect(reverse('messageapp:messages', kwargs={'dialog_id': dialog_id}))


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
