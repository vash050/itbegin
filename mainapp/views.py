from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin

from articles.models import Article
from forumapp.models import Branch
from groupapp.models import Group
from mainapp.forms import CreateTaskForm
from mainapp.models import Task, CategoryTask


def index(request):
    """
    main page
    """
    title = 'главная'
    news = Article.objects.filter(has_unpublished_changes=0)[:3]
    forum = Branch.objects.all()[0:3]
    content = {
        "title": title,
        "article_list": news,
        "forum": forum,
    }
    return render(request, 'mainapp/index.html', context=content)


def about(request):
    title = 'главная'
    content = {
        "title": title,
    }
    return render(request, 'mainapp/about.html', context=content)


class CategoryTaskMixin(MultipleObjectMixin):
    """
    Category tasks
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_task'] = CategoryTask.objects.all()
        return context


class TaskListView(ListView, CategoryTaskMixin):
    """
    page tasks all
    """
    model = Task

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories_task'] = CategoryTask.objects.all()
    #     return context


class CategoryTaskListView(ListView, CategoryTaskMixin):
    """
    Choose category tasks
    """
    model = Task

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories_task'] = CategoryTask.objects.all()
    #     return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = self.model.objects.filter(Q(category_id=query))
        return queryset


class TaskView(DetailView):
    model = Task


@login_required
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


@login_required
def get_task(request, pk):
    """
    add task for group
    """
    try:
        group_user = Group.objects.filter(author=request.user)[0]
        group_user.got_task.add(Task.objects.get(id=pk))
        return HttpResponseRedirect(reverse('mainapp:task', kwargs={'pk': pk}))
    except Exception as e:
        print(e)
        return HttpResponseRedirect(reverse('mainapp:tasks'))
