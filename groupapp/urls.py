
from django.urls import path

import groupapp.views as groupapp

app_name = 'groupapp'

urlpatterns = [
    path('groups/', groupapp.groups, name='groups'),
    path('group/<int:pk>', groupapp.group, name='group'),
    path('create_group/', groupapp.create_group, name='create_group'),
]
