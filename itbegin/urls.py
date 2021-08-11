from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from wagtail.admin import urls as wagtailadmin_urls

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
]
urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
