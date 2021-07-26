from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from .yasg import urlpatterns as doc_urls



urlpatterns = [
    path('', include('mainapp.urls'), name='mainapp'),
    path('auth/', include('authapp.urls'), name='authapp'),
    path('group/', include('groupapp.urls'), name='groupapp'),
    path('message/', include('messegeapp.urls'), name='messegeapp'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('articles/', include('articles.urls'), name='articles'),
    path('cms/', include(wagtailadmin_urls), name='cms'),
    path('documents/', include(wagtaildocs_urls)),
]
urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
