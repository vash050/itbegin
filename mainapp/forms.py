from django.forms import ModelForm

from mainapp.models import Task


class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('category', 'name', 'short_description', 'full_description', 'tz', 'professions')

    def __init__(self, *args, **kwargs):
        super(CreateTaskForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input_type_black registration__form_input"
