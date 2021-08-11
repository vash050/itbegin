from django.urls import path

import forumapp.views as forumapp

app_name = 'forunapp'

urlpatterns = [
    path('forum/', forumapp.ForumTopicList.as_view(), name='forum'),
    path('branch/', forumapp.ForumBranchList.as_view(), name='branch'),
    path('forum_message/<int:topic_id>/', forumapp.ForumMessageList.as_view(), name='forum_message'),
]
