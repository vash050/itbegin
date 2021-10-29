from django import template

from mailingapp.forms import MailContactForm

register = template.Library()


@register.inclusion_tag("mailingapp/tags/form.html")
def mail_contact_form():
    return {"mail_contact_form": MailContactForm()}
