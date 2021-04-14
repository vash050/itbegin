from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from mainapp.forms import CreateTaskForm
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


def task(request, pk):
    title = 'задача'
    task_obj = Task.objects.get(pk=pk)

    content = {'title': title, 'task': task_obj}
    return render(request, 'mainapp/task.html', context=content)


def create_task(request):
    title = 'создание задачи'

    if request.method == "POST":
        create_task_form = CreateTaskForm(request.POST, request.FILES)
        if create_task_form.is_valid():
            new_task = create_task_form.save(commit=False)
            new_task.author = request.user
            new_task.save()

            return HttpResponseRedirect(reverse('mainapp:tasks'))

    else:
        create_task_form = CreateTaskForm()

    content = {'title': title, 'create_task_form': create_task_form}

    return render(request, "mainapp/create_task.html", context=content)
