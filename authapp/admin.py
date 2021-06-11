from django.contrib import admin

from .models import SiteUser, ContactUser, Professions

admin.site.register(SiteUser)
admin.site.register(ContactUser)
admin.site.register(Professions)
