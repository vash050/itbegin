from django.urls import path

import messageapp.views as messageapp

app_name = 'messageapp'

urlpatterns = [
    path('dialogs/', messageapp.DialogsView.as_view(), name='dialog'),
    path('dialogs/creare/<int:user_id>/', messageapp.CreateDialogView.as_view(), name='create_dialog'),
    path('dialogs/<int:dialog_id>/', messageapp.MessagesView.as_view(), name='messages'),
]
