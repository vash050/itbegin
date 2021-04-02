from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class SiteUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(SiteUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ('username', 'password')
