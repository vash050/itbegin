from django.views.generic import ListView, DetailView

from articles.models import HomePage


class ArticleView(ListView):
    model = HomePage


class ArticlePage(DetailView):
    model = HomePage
