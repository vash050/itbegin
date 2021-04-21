from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.models import Professions
from groupapp.forms import CreateGroup
from groupapp.models import Group


def groups(request):
    title = 'команды'
    groups = Group.objects.all()

    content = {'title': title, 'groups': groups}
    return render(request, 'groupapp/groups.html', context=content)


def group(request, pk):
    title = 'команда'
    this_group = Group.objects.get(pk=pk)

    content = {'title': title, 'this_group': this_group}
    return render(request, 'groupapp/group.html', context=content)


def create_group(request):
    title = "создание команды"

    if request.method == "POST":
        create_group_form = CreateGroup(request.POST, request.FILES)

        if create_group_form.is_valid():
            new_group = create_group_form .save(commit=False)
            new_group.author = request.user
            new_group.save()
        return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        create_group_form = CreateGroup()

    content = {
        "title": title,
        "create_group_form": create_group_form
    }
    return render(request, "groupapp/create_group.html", content)
