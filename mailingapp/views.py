from django.views.generic import CreateView

from mailingapp.forms import MailContactForm
from mailingapp.models import MailContact


class MailContactView(CreateView):
    model = MailContact
    form_class = MailContactForm
    success_url = "/"
