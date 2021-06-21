from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput

from groupapp.models import Group, Professions, DescriptionNeedProfessions, ApplicationToNeedProfession


class CreateGroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'description', 'need_profession', 'logotype')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input_type_black registration__form_input"


class UpdateVacancyForm(ModelForm):
    class Meta:
        model = DescriptionNeedProfessions
        fields = ['id', 'group', 'profession', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input_type_black registration__form_input"


class CreateApplicationToNeedProfessionForm(ModelForm):
    class Meta:
        model = ApplicationToNeedProfession
        fields = ['description_self']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input_type_black registration__form_input"
            if field_name == 'author_application':
                field.widget = HiddenInput()
