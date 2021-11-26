from django.urls import path, include
from leads.views import list_all_leads, detail_lead, create_lead

app_name = 'leads'

urlpatterns = [
    path('', list_all_leads, name='list_lead'),
    path('detail/<int:id>', detail_lead, name='detail_lead'),
    path('create/', create_lead, name='create_lead')
]