from django.urls import path, include


from wagtail.core import urls as wagtail_urls

import articles.views as articles

app_name = 'articles'

urlpatterns = [
    path('pages/', articles.ArticleView.as_view(), name='articles'),
    path('page/<int:pk>/', articles.ArticlePage.as_view(), name='article'),
]