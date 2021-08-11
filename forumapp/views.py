from django.shortcuts import render
from django.views.generic import ListView

from forumapp.models import MainTopic


class ForumTopicList(ListView):
    model = MainTopic
