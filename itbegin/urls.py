from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from wagtail.admin import urls as wagtailadmin_urls
from django.contrib.auth import views as auth_views

from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('', include('mainapp.urls'), name='mainapp'),
    path('auth/', include('authapp.urls'), name='authapp'),
    path('group/', include('groupapp.urls'), name='groupapp'),
    path('message/', include('messageapp.urls'), name='messageapp'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('articles/', include('articles.urls'), name='articles'),
    path('wagtail_admin/', include(wagtailadmin_urls)),
    path('chat/', include('chatapp.urls'), name='chatapp'),
    path('forum/', include('forumapp.urls'), name='forumapp'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='mainapp/password/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="mainapp/password/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='mainapp/password/password_reset_complete.html'),
         name='password_reset_complete'),
]
urlpatterns += doc_urls

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [re_path(r"^__debug__/", include(debug_toolbar.urls))]
