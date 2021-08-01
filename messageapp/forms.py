from django.forms.models import ModelForm
from messageapp.models import Message, Dialog


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ""}

