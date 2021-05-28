from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, UpdateView

from authapp.models import Professions, SiteUser
from groupapp.forms import CreateGroupForm
from groupapp.models import Group


def groups(request):
    title = 'команды'
    groups = Group.objects.filter(is_active=True)

    content = {'title': title, 'groups': groups}
    return render(request, 'groupapp/groups.html', context=content)


def group(request, pk):
    title = 'команда'
    this_group = Group.objects.get(pk=pk)
    need_professions = this_group.need_profession.all()
    team_professions = SiteUser.objects.get(id=request.user.id).profession.all()
    members = SiteUser.objects.filter(group__team_members__group=pk)

    content = {
        'title': title,
        'this_group': this_group,
        'need_professions': need_professions,
        'team_professions': team_professions,
        'members': members
    }
    return render(request, 'groupapp/group.html', context=content)


def create_group(request):
    title = "создание команды"

    if request.method == "POST":
        create_group_form = CreateGroupForm(request.POST, request.FILES)

        if create_group_form.is_valid():
            new_group = create_group_form.save(commit=False)
            new_group.author = request.user
            new_group.save()
            new_group.need_profession.add(*create_group_form.data.getlist('need_profession'))
            return HttpResponseRedirect(reverse('groupapp:groups'))
    else:
        create_group_form = CreateGroupForm()

    content = {
        "title": title,
        "forms": create_group_form
    }
    return render(request, "groupapp/create_group.html", content)


class SettingView(ListView):
    model = Group


# def update_vacancy(request, pk):
#     title = 'Описание вакансий'
#
#     this_group = Group.objects.get(pk=pk)
#     need_professions = this_group.need_profession.all()
#
#     if request.method == "POST":
#         pass
#     else:
#        pass
#
#     content = {
#         'title': title,
#         # 'this_group': this_group,
#         # 'need_professions': need_professions,
#         'forms': form,
#     }
#     return render(request, 'groupapp/group_form.html', context=content)


def create_request_in_team(request):
    pass
