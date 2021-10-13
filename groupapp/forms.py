from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput, CheckboxSelectMultiple

from authapp.models import Professions
from groupapp.models import Group, DescriptionNeedProfessions, ApplicationToNeedProfession


class CreateGroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'description', 'need_profession', 'logotype')
        widgets = {
            'need_profession': CheckboxSelectMultiple(attrs={}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input_type_black registration__form_input"
            if field_name == 'need_profession':
                field.widget.attrs["class"] = "input_type_checkbox"


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
            if field_name == 'description_self':
                field.label = 'расскажите о себе'


class SearchGroupProfForm(ModelForm):
    class Meta:
        model = Professions
        fields = ('profession_name',)