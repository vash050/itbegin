from django import forms
from django.forms import ModelForm
from django.template.context_processors import request

from mainapp.models import Task


class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'short_description', 'full_description', 'tz', 'professions')

    def __init__(self, *args, **kwargs):
        super(CreateTaskForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
