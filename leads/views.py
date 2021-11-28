from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, HttpResponse, reverse
from django.views.generic.base import TemplateView
from leads.models import Agent, Lead
from leads.forms import LeadForm, CustomUserModelForm
from agents.mixins import LoginOrganiserRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic

class UserCreateClassView(generic.CreateView):
    template_name = 'registration/singup.html'
    form_class = CustomUserModelForm

    def get_success_url(self):
        return reverse('leads:list_lead')

class LandingPageClassView(generic.TemplateView):
    template_name = 'landing.html'

class ListLeadsClassView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/list_lead.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user

        if (user.is_organisor):
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = Lead.objects.filter(agent__user=user)
        return queryset

class CreateLeadsClassView(LoginOrganiserRequiredMixin, generic.CreateView):
    template_name = 'leads/create_lead.html'
    form_class = LeadForm

    def get_success_url(self):
        return reverse('leads:list_lead')

class DetailLeadClassView(LoginRequiredMixin, generic.DetailView):
    template_name = 'leads/detail_lead.html'
    context_object_name = 'lead'

    def get_queryset(self):
        user = self.request.user

        if (user.is_organisor):
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = Lead.objects.filter(agent__user=user)
        return queryset

class UpdateLeadClassView(LoginOrganiserRequiredMixin, generic.UpdateView):
    template_name = 'leads/update_lead.html'
    form_class = LeadForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:list_lead')

class DeleteLeadClassView(LoginOrganiserRequiredMixin, generic.DeleteView):
    queryset = Lead.objects.all()
    template_name = 'leads/lead_delete.html'

    def get_success_url(self):
        return reverse('leads:list_lead')
