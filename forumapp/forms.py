from django.forms import ModelForm

from forumapp.models import ForumMessage


class CreateForumMessage(ModelForm):
    class Meta:
        model = ForumMessage
        fields = ('body',)
