import hashlib
import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authapp.models import SiteUser


class SiteUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(SiteUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = SiteUser
        fields = ('username', 'password')


class SiteUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SiteUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    def save(self):
        user = super(SiteUserRegisterForm, self).save()

        user.is_active = True
        salt = hashlib.sha1(str(random.random()).encode('utf')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user

    class Meta:
        model = SiteUser
        fields = ('first_name', 'last_name', 'date_born', 'username', 'password1', 'password2',)
