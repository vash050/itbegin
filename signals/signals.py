from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from groupapp.models import ApplicationToNeedProfession, MemberTeam, DescriptionNeedProfessions


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


