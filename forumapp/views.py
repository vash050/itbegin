from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView

from forumapp.forms import CreateForumMessage
from forumapp.models import MainTopic, Branch, ForumMessage


class ForumTopicList(ListView):
    """main chapters of forum"""
    model = MainTopic


class ForumBranchList(ListView):
    """
    chapters of main chapters of forum
    """
    model = Branch

    def get_queryset(self):
        queryset = self.model.objects.filter(topic_id=self.kwargs['pk'])
        return queryset


class ForumMessageList(View):
    """
    message in branch of forum. read and create.
    """

    def get(self, request, topic_id):
        object_list = ForumMessage.objects.filter(topic_id=topic_id)
        context = {
            'user_profile': request.user,
            'object_list': object_list,
            'topic_pk': topic_id,
            'form': CreateForumMessage()
        }
        return render(request, 'forumapp/forummessage_list.html', context=context)

    def post(self, request, topic_id):
        form = CreateForumMessage(data=request.POST)
        branch = Branch.objects.get(id=topic_id)
        if form.is_valid():
            message = form.save(commit=False)
            message.topic = branch
            message.author_branch_forum = request.user
            message.save()
        context = {
            'topic_id': topic_id,
        }
        return redirect(reverse('forunapp:forum_message', kwargs=context))

    @method_decorator(user_passes_test(lambda x: x.is_authenticated))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
