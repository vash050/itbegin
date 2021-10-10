from django.conf.urls import url
from django.urls import path, re_path

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('profile/', authapp.profile, name='profile'),
    path('register/', authapp.register, name='register'),
    path('logout/', authapp.logout, name='logout'),
    path('update/', authapp.update, name='update'),
    path('profile/<int:pk>/', authapp.UserProfile.as_view(), name='user_profile'),
    path('setting_user/<int:pk>/', authapp.UserSetting.as_view(), name='setting_user'),
    path('up_setting_user_cont/<int:pk>/', authapp.UpdateUserContact.as_view(), name='up_setting_user_cont'),
    path('change_password/', authapp.ChangePassword.as_view(), name='change_password'),
    url(r'^authapp/login/.?', authapp.login),
    re_path(r"^verify/(?P<email>.+)/(?P<activation_key>\w+)/$", authapp.verify, name="verify"),
]
