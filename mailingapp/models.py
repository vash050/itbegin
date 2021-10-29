from django.db import models


class MailContact(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
