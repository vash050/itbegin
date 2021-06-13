from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from authapp.models import SiteUser
from groupapp.forms import CreateGroupForm, UpdateVacancyForm
from groupapp.models import Group, DescriptionNeedProfessions


def groups(request):
    title = 'команды'
    groups = Group.objects.filter(is_active=True)

    content = {'title': title, 'object_list': groups}
    return render(request, 'groupapp/groups.html', context=content)


class UserGroupView(ListView):
    model = Group
    template_name = 'groupapp/groups.html'

    def get_queryset(self):
        return Group.objects.filter(author=self.request.user)


# def create_group(request):
#     title = "создание команды"
#
#     if request.method == "POST":
#         create_group_form = CreateGroupForm(request.POST, request.FILES)
#
#         if create_group_form.is_valid():
#             new_group = create_group_form.save(commit=False)
#             new_group.author = request.user
#             new_group.save()
#             new_group.need_profession.add(*create_group_form.data.getlist('need_profession'))
#             return HttpResponseRedirect(reverse('groupapp:groups'))
#     else:
#         create_group_form = CreateGroupForm()
#
#     content = {
#         "title": title,
#         "object_list": create_group_form
#     }
#     return render(request, "groupapp/create_group.html", content)

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


def create_request_in_team(request):
    pass
