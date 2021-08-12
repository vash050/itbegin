from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView

from forumapp.forms import CreateForumMessage
from forumapp.models import MainTopic, Branch, ForumMessage


class ForumTopicList(ListView):
    model = MainTopic


class ForumBranchList(ListView):
    model = Branch

    def get_queryset(self):
        queryset = self.model.objects.filter(topic_id=self.kwargs['pk'])
        return queryset


class ForumMessageList(View):
    def get(self, request, topic_id):
        object_list = ForumMessage.objects.filter(topic_id=topic_id)
        context = {
            'user_profile': request.user,
            'object_list': object_list,
            'topic_pk': topic_id,
            'form': CreateForumMessage()
        }
        print(object_list)
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
