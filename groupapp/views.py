from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from authapp.models import SiteUser, Professions
from groupapp.forms import CreateGroupForm, UpdateVacancyForm, CreateApplicationToNeedProfessionForm, \
    SearchGroupProfForm
from groupapp.models import Group, DescriptionNeedProfessions, ApplicationToNeedProfession
from groupapp.serializers import ApplicationsToTeamSerializer
from mainapp.models import Task


def groups(request, page_num=1):
    """
    постраничный вывод команд
    """
    title = 'команды'
    groups = Group.objects.filter(is_active=True).order_by('date_create')

    groups_paginator = Paginator(groups, 3)
    try:
        groups = groups_paginator.page(page_num)
    except PageNotAnInteger:
        groups = groups_paginator.page(1)
    except EmptyPage:
        groups = groups_paginator.page(groups_paginator.num_pages)

    content = {'title': title, 'page_obj': groups}
    return render(request, 'groupapp/groups.html', context=content)


def user_groups(request, page_num=1):
    """
    вывод команд в который пользователь состоит или является основателем
    """
    title = 'команды'
    groups = Group.objects.filter(author=request.user).order_by('date_create')

    groups_paginator = Paginator(groups, 3)
    try:
        groups = groups_paginator.page(page_num)
    except PageNotAnInteger:
        groups = groups_paginator.page(1)
    except EmptyPage:
        groups = groups_paginator.page(groups_paginator.num_pages)

    content = {'title': title, 'page_obj': groups}
    return render(request, 'groupapp/mygroups.html', context=content)


class GroupCreateView(CreateView):
    model = Group
    form_class = CreateGroupForm
    template_name = 'groupapp/create_group.html'

    # success_url = reverse_lazy('groupapp:groups')

    def post(self, request, *args, **kwargs):
        '''
        added to the method author=user
        '''
        form = self.get_form()
        if form.is_valid():
            new_group = form.save(commit=False)
            new_group.author = request.user
            new_group.save()
            new_group.need_profession.add(*form.data.getlist('need_profession'))
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def group(request, pk):
    """
    вывод страницы конкретной команды
    """
    title = 'команда'
    this_group = Group.objects.get(pk=pk)
    team_professions = SiteUser.objects.get(id=request.user.id).profession.all()
    members = SiteUser.objects.filter(memberteam__group_id=pk)
    professions_all = DescriptionNeedProfessions.objects.filter(group_id=pk)
    need_professions = professions_all.filter(status=0)
    occupied_vacancy = professions_all.filter(status=1)

    content = {
        'title': title,
        'this_group': this_group,
        'need_professions': need_professions,
        'occupied_vacancy': occupied_vacancy,
        'team_professions': team_professions,
        'members': members
    }
    return render(request, 'groupapp/group.html', context=content)


class GroupUpdateView(UpdateView):
    model = Group
    form_class = CreateGroupForm
    template_name = 'groupapp/create_group.html'
    success_url = reverse_lazy('groupapp:groups')


class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('groupapp:groups')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)


class SettingView(ListView):
    """
    page setting group
    """
    model = Group


class VacancyUpdate(UpdateView):
    """
    form description vacancy of group
    """
    model = Group
    fields = []
    success_url = reverse_lazy('groupapp:groups')

    def get_context_data(self, **kwargs):
        data = super(VacancyUpdate, self).get_context_data(**kwargs)
        VacancyFormSet = inlineformset_factory(Group, DescriptionNeedProfessions, form=UpdateVacancyForm, extra=1)
        pk = self.kwargs.get('pk')

        if self.request.POST:
            formset = VacancyFormSet(self.request.POST, instance=Group.objects.get(id=pk))
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
        data['vacancyneed'] = formset
        return data

    def form_valid(self, form):
        """need refactor"""
        if form.is_valid:
            my_list = []
            a = []
            for key, el in form.data.items():
                if key[33:] == 'description':
                    a.append(el)
                if key[33:] == 'id':
                    a.append(el)
                    my_list.append(a)
                    a = []
            for el in my_list:
                idx = int(el[1])
                dis = el[0]
                f = DescriptionNeedProfessions.objects.get(id=idx)
                f.description = dis
                f.save()
            form.save()
            return super().form_valid(form)


class NeedProfessionDescriptionView(DetailView):
    model = DescriptionNeedProfessions


def create_application_need_prof(request, pk):
    """
    создание заявки на вакансию в команду
    """
    need_prof_pk = pk

    if request.method == "POST":
        form = CreateApplicationToNeedProfessionForm(request.POST, request.FILES)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.to_need_profession = DescriptionNeedProfessions.objects.get(id=pk)
            new_form.author_application = request.user
            new_form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = CreateApplicationToNeedProfessionForm()

    content = {
        "need_prof_pk": need_prof_pk,
        "forms": form
    }
    return render(request, "groupapp/applicationtoneedprofession_form.html", content)


class ApplicationsToTeamsView(ListView):
    """
    заявки в команду
    """
    model = ApplicationToNeedProfession

    def get_queryset(self):
        queryset = self.model.objects.filter(to_need_profession__group=self.kwargs['pk'])
        return queryset


class UpdateApplicationsFromTeamApi(RetrieveUpdateDestroyAPIView):
    """

    """
    queryset = ApplicationToNeedProfession.objects.all()
    serializer_class = ApplicationsToTeamSerializer


class TaskGroupList(ListView):
    """
    задачи взятые командой
    """
    model = Task
    template_name = 'groupapp/taskforgroup.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(got_task=self.kwargs['pk'])
        return queryset


class SearchGroupName(ListView):
    model = Group
    template_name = 'groupapp/search_groups.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = self.model.objects.filter(Q(name=query))
        return queryset


def search_group_by_name(request):
    return render(request, "groupapp/search_name_form.html")


class ChoiceVacation(ListView):
    model = Professions


class SearchGroupProf(ListView):
    model = Group
    template_name = 'groupapp/search_groups.html'

    def get_queryset(self):
        """
        метод нужно оптимизировать
        :return:
        """
        query = int(self.request.GET.get('q'))
        id_group = DescriptionNeedProfessions.objects.filter(Q(status=0) & Q(profession=query))
        print(id_group)
        queryset = []
        for el in id_group:
            queryset.append(Group.objects.get(id=el.group.id))
        print(queryset)
        return queryset
