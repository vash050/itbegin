import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from articles.models import Article
from authapp.models import SiteUser
from forumapp.models import Branch
from groupapp.models import Group
from mainapp.forms import CreateTaskForm
from mainapp.models import Task, CategoryTask

import logs.log_conf

SERVER_LOGGER = logging.getLogger('server')


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


class TaskUpdateView(UpdateView):
    model = Task
    form_class = CreateTaskForm


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('mainapp:tasks')


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


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            SERVER_LOGGER.info(f"форма адреса для васстоновления пароля валидна")
            data = password_reset_form.cleaned_data['email']
            associated_users = SiteUser.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "mainapp/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    SERVER_LOGGER.info(f'"email": {user.email}, "user": {user}')
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError as e:
                        SERVER_LOGGER.critical(f"ошибка отправки письма восстановления пароля {e.args}")
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="mainapp/password/password_reset.html",
                  context={"password_reset_form": password_reset_form})


def send_mail_reg(request):
    """
    страница с сообщение об отправлении письма для подтверждения регистрации
    """
    title = 'письмо отправлено'

    content = {
        "title": title,
    }
    return render(request, 'mainapp/password/send_mail_reg.html', context=content)
