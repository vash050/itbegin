import hashlib
import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms.widgets import HiddenInput, TextInput, PasswordInput

from authapp.models import SiteUser
from groupapp import forms


class SiteUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input_type_black registration__form_input"


class SiteUserRegisterForm(UserCreationForm):
    class Meta:
        model = SiteUser
        fields = ('first_name', 'last_name', 'date_born', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input_type_black registration__form_input"

    def save(self):
        user = super(SiteUserRegisterForm, self).save()

        user.is_active = True
        salt = hashlib.sha1(str(random.random()).encode('utf')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user


class SiteUserUpdateForm(UserChangeForm):
    class Meta:
        model = SiteUser
        fields = ('first_name', 'last_name', 'date_born', 'username',
                  'profession', 'about_me', 'link_to_portfolio')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input_type_black registration__form_input"

