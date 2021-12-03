from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, HttpResponse, reverse
from django.views.generic.base import TemplateView
from leads.models import Agent, Category, Lead
from leads.forms import LeadUpdateCategoryForm, LeadForm, CustomUserModelForm, AssingAgentToLeadForm
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
            queryset = Lead.objects.filter(
                organisation=user.userprofile, 
                agent__isnull=False
            )
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation, 
                agent__isnull=False
            )
            queryset = Lead.objects.filter(agent__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListLeadsClassView, self).get_context_data(**kwargs)
        user = self.request.user

        if (user.is_organisor):
            queryset = Lead.objects.filter(
                organisation=user.userprofile, 
                agent__isnull=True
            )
            context.update({
                'unassigned_leads':queryset
            })

        return context

class CreateLeadsClassView(LoginOrganiserRequiredMixin, generic.CreateView):
    template_name = 'leads/create_lead.html'
    form_class = LeadForm

    def get_success_url(self):
        return reverse('leads:list_lead')

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organisation = self.request.user.userprofile
        lead.save()

        return super(CreateLeadsClassView, self).form_valid(form)

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

class AssingAgentToLeadView(LoginOrganiserRequiredMixin, generic.FormView):
    template_name = 'leads/assign_lead.html'
    form_class = AssingAgentToLeadForm

    def get_success_url(self):
        return reverse('leads:list_lead')

    def get_form_kwargs(self):
        kwargs = super(AssingAgentToLeadView, self).get_form_kwargs()

        kwargs.update({
            'request':self.request
        })
        
        return kwargs

    def form_valid(self, form):
        lead = Lead.objects.get(id=self.kwargs['pk'])
        lead.agent = form.cleaned_data['agents']
        lead.save()
        return super(AssingAgentToLeadView, self).form_valid(form)

class ListUnassignedLeadsClassView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/unassigned_listleads.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user

        if (user.is_organisor):
            queryset = Lead.objects.filter(
                organisation=user.userprofile, 
                agent__isnull=False
            )
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation, 
                agent__isnull=False
            )
            queryset = Lead.objects.filter(agent__user=user)

        queryset.filter(category__isnull=True)
    
        return queryset


class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        user = self.request.user

        if (user.is_organisor):
            queryset = Category.objects.filter(
                organisation=user.userprofile, 
            )
        else:
            queryset = Category.objects.filter(
                organisation=user.agent.organisation, 
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)

        user = self.request.user

        if (user.is_organisor):
            queryset = Lead.objects.filter(
                organisation=user.userprofile, 
            )
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation, 
            )

        context.update({
            "unassigned_leads_count": queryset.filter(category__isnull=True).count()
        })

        return context


class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'leads/category_detail.html'
    object_context_name = 'category'

    def get_queryset(self):
        user = self.request.user

        if (user.is_organisor):
            queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            queryset = Category.objects.filter(organisation=user.agent.organisation)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)

        new_context = Lead.objects.filter(category=self.get_object()).all()

        context.update({
            'leads':new_context
        })

        return context
        
class CategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/leadcategory_update.html'
    form_class = LeadUpdateCategoryForm

    def get_success_url(self):
        return reverse('leads:detail_lead', kwargs={'pk': self.get_object().id})

    def get_queryset(self):
        user = self.request.user

        if (user.is_organisor):
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = Lead.objects.filter(agent__user=user)

        return queryset