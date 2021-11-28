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
        print(Agent.objects.filter(organisation=organisation))
        return Agent.objects.filter(organisation=organisation)

class AgentCreateView(LoginOrganiserRequiredMixin, generic.CreateView):
    template_name = 'agents/create_agent.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent_list')

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
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