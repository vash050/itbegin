import hashlib
import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms.widgets import HiddenInput, CheckboxSelectMultiple, DateInput
from django import forms

from authapp.models import SiteUser, ContactUser

class DateInput(forms.DateInput):
    input_type = 'date'


class SiteUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input_type_black registration__form_input"


class SiteUserRegisterForm(UserCreationForm):
    class Meta:
        model = SiteUser
        fields = ('first_name', 'last_name', 'date_born', 'username', 'email', 'password1', 'password2')
        widgets = {
            'date_born': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input_type_black registration__form_input"
            if field_name == 'password1':
                field.help_text = "Пароль не должен быть слишком похож на другую вашу личную информацию. Ваш пароль " \
                                  "должен содержать как минимум 8 символов. Пароль не должен быть часто используемым. " \
                                  "Пароль не может состоять только из цифр. "

    def save(self):
        user = super(SiteUserRegisterForm, self).save()

        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user


class SiteUserUpdateForm(UserChangeForm):
    class Meta:
        model = SiteUser
        fields = ('avatar', 'first_name', 'last_name', 'date_born', 'username',
                  'profession', 'about_me', 'link_to_portfolio')
        widgets = {
            'profession': CheckboxSelectMultiple(attrs={}),
            'date_born': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input_type_black registration__form_input"
            if field_name == 'password':
                field.widget = HiddenInput()
            if field_name == 'profession':
                field.widget.attrs["class"] = "input_type_checkbox"
            



class SiteUserUpdateContact(UserChangeForm):
    class Meta:
        model = ContactUser
        fields = ('user_phone', 'user_instagram', 'user_vk', 'user_telegram')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input_type_black registration__form_input"
            if field_name == 'password':
                field.widget = HiddenInput()
