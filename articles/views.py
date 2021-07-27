from django.conf import settings
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticleView(ListView):
    """
    output published articles only
    """
    model = Article
    queryset = Article.objects.filter(has_unpublished_changes=0)


class ArticlePage(DetailView):
    model = Article


class MyArticleListView(ListView):
    model = Article

    def get_queryset(self):
        queryset = Article.objects.filter(owner=self.request.user)
        return queryset


def author_create(request):
    """
    author(user) add to group editors
    :param request:
    :return:
    """
    Group.objects.get(pk=2).user_set.add(request.user)
    return HttpResponseRedirect(reverse('authapp:profile'))
