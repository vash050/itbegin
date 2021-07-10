
from django.urls import path

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('profile/', authapp.profile, name='profile'),
    path('register/', authapp.register, name='register'),
    path('logout/', authapp.logout, name='logout'),
    path('update/', authapp.update, name='update'),
    path('profile/<int:pk>/', authapp.UserProfile.as_view(), name='user_profile'),
]
