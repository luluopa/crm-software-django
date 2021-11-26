from django.urls import path, include
from leads.views import delete_lead, list_all_leads, detail_lead, create_lead, update_lead

app_name = 'leads'

urlpatterns = [
    path('', list_all_leads, name='list_lead'),
    path('detail/<int:id>', detail_lead, name='detail_lead'),
    path('create/', create_lead, name='create_lead'),
    path('update/<int:id>', update_lead, name='update_lead'),
    path('delete/<int:id>', delete_lead, name='delete_lead')
]