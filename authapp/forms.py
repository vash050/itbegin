import hashlib
import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms.widgets import HiddenInput, TextInput, PasswordInput

from authapp.models import SiteUser
from groupapp import forms


class SiteUserLoginForm(AuthenticationForm):
    class Meta:
        model = SiteUser
        fields = ('username', 'password')

    # def __init__(self, *args, **kwargs):
    #     super(SiteUserLoginForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs["class"] = "form-control"


class SiteUserRegisterForm(UserCreationForm):
    class Meta:
        model = SiteUser
        fields = ('first_name', 'last_name', 'date_born', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SiteUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ""

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
        fields = ('avatar', 'first_name', 'last_name', 'date_born', 'username', 'password',
                  'profession', 'about_me', 'link_to_portfolio', 'free')

    def __init__(self, *args, **kwargs):
        super(SiteUserUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input_type_white registration__form_input"
            field.help_text = ""
            if field_name == 'password':
                field.widget = HiddenInput()
