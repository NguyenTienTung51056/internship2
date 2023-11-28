from django.views.generic import ListView, DetailView
from .models import Person, Group

class PersonListView(ListView):
    model = Person
    template_name = 'person_list.html'
    context_object_name = 'persons'

    def get_queryset(self):
        # Fetch related groups for each person
        return Person.objects.prefetch_related('group_set').all()

class PersonDetailView(DetailView):
    model = Person
    template_name = 'apps/person_detail.html'
    context_object_name = 'person'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch related groups for the person
        context['related_groups'] = self.object.group_set.all()
        return context

class GroupListView(ListView):
    model = Group
    template_name = 'group_list.html'
    context_object_name = 'group_list'

class GroupDetailView(DetailView):
    model = Group
    template_name = 'apps/group_detail.html'
    context_object_name = 'group'
