from django.contrib import admin

from forumapp.models import MainTopic, SubTopic, Branch, ForumMessage

admin.site.register(MainTopic)
admin.site.register(SubTopic)
admin.site.register(Branch)
admin.site.register(ForumMessage)
