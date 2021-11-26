from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from leads.models import Agent, Lead
from leads.forms import LeadForm

def landing_page(request):
    return render(request, 'landing.html', {})

def list_all_leads(request):
    leads = Lead.objects.all()

    context = {
        'leads':leads
    }

    return render(request, 'leads/list_lead.html', context)

def detail_lead(request, id):
    lead = Lead.objects.get(id=id)

    context = {
        'lead':lead
    }

    return render(request, 'leads/detail_lead.html', context)

def create_lead(request):
    lead_form_instance = LeadForm()

    if request.method == 'POST':
        lead_form_instance = LeadForm(request.POST)

        if lead_form_instance.is_valid():
            lead_form_instance.save()
            return redirect('/leads')

    context = {
        'form':lead_form_instance
    }
    
    return render(request, 'leads/create_lead.html', context)

def update_lead(request, id):
    lead_instance = Lead.objects.get(id=id)
    lead_form_instance = LeadForm(instance=lead_instance)

    if request.method == 'POST':
        lead_form_instance = LeadForm(request.POST, instance=lead_instance)

        if lead_form_instance.is_valid():
            lead_form_instance.save()
            return redirect('/leads')

    context = {
        'form':lead_form_instance,
        'lead':lead_instance
    }
    
    return render(request, 'leads/update_lead.html', context)

def delete_lead(request, id):
    lead_instance = Lead.objects.get(id=id)
    lead_instance.delete()
    return redirect('/leads')