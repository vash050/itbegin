from django.forms.models import ModelForm

from groupapp.models import Group


class CreateGroup(ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'description', 'need_profession','logotype')

