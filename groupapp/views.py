from django.shortcuts import render

from authapp.models import Professions
from groupapp.models import Group


def groups(request):
    title = 'команды'
    groups = Group.objects.all()

    content = {'title': title, 'groups': groups}
    return render(request, 'groupapp/groups.html', context=content)