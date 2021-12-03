from django.urls import path, include
from leads.views import (DeleteLeadClassView, ListLeadsClassView, 
                        DetailLeadClassView, CreateLeadsClassView, UpdateLeadClassView,
                        AssingAgentToLeadView, CategoryListView, CategoryDetailView,
                        ListUnassignedLeadsClassView, CategoryUpdateView)

app_name = 'leads'

urlpatterns = [
    path('', ListLeadsClassView.as_view(), name='list_lead'),
    path('detail/<int:pk>', DetailLeadClassView.as_view(), name='detail_lead'),
    path('create/', CreateLeadsClassView.as_view(), name='create_lead'),
    path('update/<int:pk>', UpdateLeadClassView.as_view(), name='update_lead'),
    path('delete/<int:pk>', DeleteLeadClassView.as_view(), name='delete_lead'),
    path('assing_lead/<int:pk>', AssingAgentToLeadView.as_view(), name='assign_lead'),
    path('categories/', CategoryListView.as_view(), name='list_category'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='detail_category'),
    path('categories/unassigned_leads/', ListUnassignedLeadsClassView.as_view(), name='unassigned_listleads'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='update_category'),
]