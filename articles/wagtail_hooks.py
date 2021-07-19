from django.contrib.auth.models import Group
from wagtail.core import hooks


@hooks.register('after_create_user')
def add_user_to_group(request, user):
    if user:
        group, created = Group.objects.get_or_create(name='Editors')
        user.groups.add(group)
