from django.forms.models import ModelForm
from messegeapp.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['massage']
        labels = {'massage': ""}
