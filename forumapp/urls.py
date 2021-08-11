from django.urls import path

import forumapp.views as forumapp

app_name = 'forunapp'

urlpatterns = [
    path('forum/', forumapp.ForumTopicList.as_view(), name='forum'),
]