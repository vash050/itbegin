from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from mailingapp.models import MailContact


class MailContactForm(forms.ModelForm):
    """
    Форма подписки на email
    """
    # captcha = ReCaptchaField()

    class Meta:
        model = MailContact
        fields = ('email',)
        widgets = {
            'email': forms.TextInput(attrs={"class": "input_type_white footer__subscribe-input"})
        }
