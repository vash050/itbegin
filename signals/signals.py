from django.db.models.signals import post_save, post_init
from django.db.utils import OperationalError
from django.dispatch.dispatcher import receiver

from authapp.models import SiteUser, ContactUser
from groupapp.models import ApplicationToNeedProfession, MemberTeam


@receiver(post_save, sender=ApplicationToNeedProfession)
def add_to_team(sender, instance, **kwargs):
    """
    for groupapp
    The function receives a signal from the application model when it is updated.
     If acceptance == 1, the user is added to the team.

    :param sender: model ApplicationToNeedProfession
    :param instance: Application
    """
    if instance.acceptation == 1:
        MemberTeam.objects.create(group_id=instance.to_need_profession.group, user_id=instance.author_application)
        obj = instance.to_need_profession
        obj.status = 1
        obj.save()


@receiver(post_save, sender=SiteUser)
def add_contact_user(sender, instance, **kwargs):
    try:
        if ContactUser.objects.get(user_id=instance.id) is None:
            ContactUser.objects.create(user_id=instance.id)
    except OperationalError as e:
        print(e)
