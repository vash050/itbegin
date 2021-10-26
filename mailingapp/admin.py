from django.contrib import admin

from .models import MailContact


@admin.register(MailContact)
class MailContactAdmin(admin.ModelAdmin):
    list_display = ('email', "date", "is_active")
