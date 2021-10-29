from django.urls import path

import mailingapp.views as mailingapp

app_name = 'mailingapp'

urlpatterns = [
    path('mailing-contact/', mailingapp.MailContactView.as_view(), name='mailing_contact'),
]