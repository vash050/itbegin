from django.shortcuts import render

from mainapp.models import Task


def index(request):
    title = 'главная'
    content = {"title": title}
    return render(request, 'mainapp/index.html', context=content)


def tasks(request):
    title = 'задачи'
    tasks = Task.objects.all()

    content = {'title': title, 'tasks': tasks}
    return render(request, 'mainapp/tasks.html', context=content)
