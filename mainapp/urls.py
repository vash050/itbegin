from django.urls import path

import authapp
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('tasks/', mainapp.tasks, name='tasks'),
]
