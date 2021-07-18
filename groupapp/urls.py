from django.urls import path
from rest_framework.routers import SimpleRouter

import groupapp.views as groupapp

app_name = 'groupapp'

router = SimpleRouter()
# router.register('api/delete_applications_to_team/<int:pk>/', groupapp.#)

urlpatterns = [
    path('groups/', groupapp.groups, name='groups'),
    path('groups/<int:page_num>/', groupapp.groups, name='groups_paginator'),
    path('create_group/', groupapp.GroupCreateView.as_view(), name='create_group'),
    path('group/<int:pk>', groupapp.group, name='group'),
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
]

urlpatterns += router.urls
