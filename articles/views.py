from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from articles.models import HomePage, Article


class ArticleView(ListView):
    model = HomePage


class ArticlePage(DetailView):
    model = HomePage


class MyArticleListView(ListView):
    model = Article


def author_create(request):
    """
    author(user) add to group editors
    :param request:
    :return:
    """
    Group.objects.get(pk=2).user_set.add(request.user)
    return HttpResponseRedirect(reverse('authapp:profile'))
