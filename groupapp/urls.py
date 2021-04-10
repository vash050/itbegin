
from django.urls import path

import groupapp.views as groupapp

app_name = 'groupapp'

urlpatterns = [
    path('groups/', groupapp.groups, name='groups'),
]
