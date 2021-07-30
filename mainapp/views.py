from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from articles.models import Article
from mainapp.forms import CreateTaskForm
from mainapp.models import Task


def index(request):
    title = 'главная'
    news = Article.objects.filter(has_unpublished_changes=0)[:3]
    content = {
        "title": title,
        "article_list": news,
    }
    return render(request, 'mainapp/index.html', context=content)


class TaskListView(ListView):
    model = Task


class TaskView(DetailView):
    model = Task


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
