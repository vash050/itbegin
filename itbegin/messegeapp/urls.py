from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path

import messegeapp.views as messegeapp


app_name = 'messegeapp'

urlpatterns = [
 url(r'^dialogs/$', login_required(messegeapp.DialogView.as_view()), name='dialogs'),
 url(r'^dialogs/create/(?P<user_id>\d+)/$', login_required(messegeapp.CreateDialogView.as_view()), name='create_dialog'),
 url(r'^dialogs/(?P<chat_id>\d+)/$', login_required(messegeapp.MessageView.as_view()), name='messages'),
 ]
