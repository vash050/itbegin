from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save, post_init
from django.db.utils import OperationalError
from django.dispatch.dispatcher import receiver

from authapp.models import SiteUser, ContactUser
from groupapp.models import ApplicationToNeedProfession, MemberTeam
from messageapp.models import Message


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
        ContactUser.objects.get(user_id=instance.id)
    except OperationalError as e:
        print(e)
    except ObjectDoesNotExist as e:
        print(e)
        ContactUser.objects.create(user_id=instance.id)


@receiver(post_save, sender=Message)
def post_save_comment(sender, instance, created, **kwargs):
    # если объект был создан
    if created:
        # указываем чату, в котором находится данное сообщение, что это последнее сообщение
        instance.dialog.last_message = instance
        # и обновляем данный внешний ключ чата
        instance.dialog.save(update_fields=['last_message'])
