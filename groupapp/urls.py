
from django.urls import path

from django.urls import path

import groupapp.views as groupapp

app_name = 'groupapp'

urlpatterns = [
    path('groups/', groupapp.groups, name='groups'),
    path('groups/<int:page_num>/', groupapp.groups, name='groups_paginator'),
    # path('create_group/', groupapp.create_group, name='create_group'),
    path('create_group/', groupapp.GroupCreateView.as_view(), name='create_group'),
    path('group/<int:pk>', groupapp.group, name='group'),
    path('update_group/<int:pk>/', groupapp.GroupUpdateView.as_view(), name='update_group'),
    path('delete_group/<int:pk>/', groupapp.GroupDeleteView.as_view(), name='delete_group'),
    path('create_request_in_team/', groupapp.create_request_in_team, name='create_request_in_team'),
    path('setting/<int:pk>/', groupapp.SettingView.as_view(), name='setting_group'),
    path('update_vacancy/<int:pk>/', groupapp.VacancyUpdate.as_view(), name='update_vacancy'),
    path('user_groups/', groupapp.user_groups, name='user_groups'),
    # path('user_groups/<int:page_num>/', groupapp.UserGroupView.as_view(), name='user_groups'),
    path('user_groups/<int:page_num>/', groupapp.user_groups, name='user_groups_paginator'),
    # path('user_groups/<str:page_num>/', groupapp.UserGroupView.as_view(), name='user_groups_paginator'),
]
