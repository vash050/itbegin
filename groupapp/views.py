from django.forms import formset_factory, inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView

from authapp.models import Professions, SiteUser
from groupapp.forms import CreateGroupForm, UpdateVacancyForm
from groupapp.models import Group, DescriptionNeedProfessions


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


class VacancyUpdate(UpdateView):
    model = Group
    fields = []
    success_url = reverse_lazy('groupapp:groups')

    def get_context_data(self, **kwargs):
        data = super(VacancyUpdate, self).get_context_data(**kwargs)
        VacancyFormSet = inlineformset_factory(Group, DescriptionNeedProfessions, form=UpdateVacancyForm, extra=1)
        pk = self.kwargs.get('pk')

        if self.request.POST:
            formset = VacancyFormSet(self.request.POST)
        else:
            need_profession = DescriptionNeedProfessions.objects.filter(group=pk)
            if len(need_profession):
                VacancyFormSet = inlineformset_factory(Group, DescriptionNeedProfessions, form=UpdateVacancyForm,
                                                       extra=len(need_profession))
                formset = VacancyFormSet()
                for el, form in enumerate(formset.forms):
                    form.initial['profession'] = need_profession[el].profession
                    form.initial['description'] = need_profession[el].description
                    form.initial['group'] = need_profession[el].group
                    form.initial['id'] = need_profession[el].id
            else:
                formset = VacancyFormSet()
        data['vacancyneed'] = formset
        return data

    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     vacancyneed = context['vacancyneed']
    #     self.object = form.save()
    #     if vacancyneed.is_valid():
    #         vacancyneed.instance = self.object
    #         vacancyneed.save()

        return super(VacancyUpdate, self).form_valid(form)


def create_request_in_team(request):
    pass
