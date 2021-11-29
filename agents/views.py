import random
from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from agents.forms import AgentModelForm
from agents.mixins import LoginOrganiserRequiredMixin

class AgentListView(LoginOrganiserRequiredMixin, generic.ListView):
    template_name = 'agents/list_agents.html'
    context_object_name = 'agents'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

class AgentCreateView(LoginOrganiserRequiredMixin, generic.CreateView):
    template_name = 'agents/create_agent.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent_list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_organisor = False
        user.is_agent = True
        user.set_password(f"{random.randint(0,10000000)}")
        user.save()

        Agent.objects.create(
            user=user,
            organisation=self.request.user.userprofile
        )

        return super(AgentCreateView, self).form_valid(form)

class AgentUpdateView(LoginOrganiserRequiredMixin, generic.UpdateView):
    template_name = 'agents/update_agent.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent_list')

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

class AgentDeleteView(LoginOrganiserRequiredMixin, generic.DeleteView):
    template_name = 'agents/delete_agent.html'
    context_object_name = 'agent'

    def get_success_url(self) -> str:
        return reverse('agents:agent_list')

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

class AgentDetailView(LoginOrganiserRequiredMixin, generic.DetailView):
    template_name = 'agents/detail_agent.html'
    queryset = Agent.objects.all()
    context_object_name = 'agent'