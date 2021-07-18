from django.views.generic import ListView

from articles.models import HomePage


class ArticleView(ListView):
    model = HomePage
