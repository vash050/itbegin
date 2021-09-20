from django.urls import path

import authapp
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('tasks/', mainapp.TaskListView.as_view(), name='tasks'),
    path('tasks_category/', mainapp.CategoryTaskListView.as_view(), name='tasks_category'),
    path('task/<int:pk>/', mainapp.TaskView.as_view(), name='task'),
    path('create_task/', mainapp.create_task, name='create_task'),
    path('get_task/<int:pk>/', mainapp.get_task, name='get_task'),
    path('about/', mainapp.about, name='about'),
]
