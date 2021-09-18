import re

from django.conf.urls import url
from django.urls import path
from rest_framework.routers import SimpleRouter

import authapp.views as authapp
import groupapp.views as groupapp

app_name = 'groupapp'

router = SimpleRouter()
# router.register('api/delete_applications_to_team/<int:pk>/', groupapp.#)

urlpatterns = [
    path('groups/', groupapp.groups, name='groups'),
    path('groups/<int:page_num>/', groupapp.groups, name='groups_paginator'),
    path('create_group/', groupapp.GroupCreateView.as_view(), name='create_group'),
    path('group/<int:pk>/', groupapp.group, name='group'),
    path('update_group/<int:pk>/', groupapp.GroupUpdateView.as_view(), name='update_group'),
    path('delete_group/<int:pk>/', groupapp.GroupDeleteView.as_view(), name='delete_group'),
    path('setting/<int:pk>/', groupapp.SettingView.as_view(), name='setting_group'),
    path('update_vacancy/<int:pk>/', groupapp.VacancyUpdate.as_view(), name='update_vacancy'),
    path('user_groups/', groupapp.user_groups, name='user_groups'),
    path('user_groups/<int:page_num>/', groupapp.user_groups, name='user_groups_paginator'),
    path('need_profession_description/<int:pk>/', groupapp.NeedProfessionDescriptionView.as_view(),
         name='need_prof_view'),
    path('create_application_need_prof/<int:pk>/', groupapp.create_application_need_prof,
         name='create_application_need_prof'),
    path('applications_to_team/<int:pk>/', groupapp.ApplicationsToTeamsView.as_view(), name='applications_to_team'),
    path('api/update_applications_to_team/<int:pk>/', groupapp.UpdateApplicationsFromTeamApi.as_view()),
    path('tasks_for_group/<int:pk>/', groupapp.TaskGroupList.as_view(), name='tasks_for_group'),
    path('search_group_name/', groupapp.SearchGroupName.as_view(), name='search_group_name'),
    path('search_group_by_name/', groupapp.search_group_by_name, name='search_group_by_name'),
    path('search_group_prof/', groupapp.ChoiceVacation.as_view(), name='search_group_prof'),
    path('search_group_by_prof/', groupapp.SearchGroupProf.as_view(), name='search_group_by_prof'),
    path('tasks_done_for_group/<int:pk>/', groupapp.TaskDoneGroupList.as_view(), name='tasks_done_for_group'),
]

urlpatterns += router.urls
