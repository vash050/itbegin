from django.urls import path

import messageapp.views as messageapp

app_name = 'messageapp'

urlpatterns = [
    path('api/dialogs/', messageapp.DialogsApi.as_view(), name='api_dialog'),
    path('dialogs/creare/<int:user_id>/', messageapp.CreateDialogView.as_view(), name='create_dialog'),
    path('api/dialogs/<int:pk>/', messageapp.MessageCreateApi.as_view(), name='api_dialog'),
    # path('dialogs/<int:dialog_id>/', messageapp.DialogsView.as_view(), name='dialog'),
]
