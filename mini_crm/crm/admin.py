from django.urls import path
from . import views
from django.contrib import admin
from .models import Contact, Lead

# Simple registration
admin.site.register(Contact)
admin.site.register(Lead)

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Contacts
    path('contacts/', views.contacts_list, name='contacts_list'),
    path('contacts/add/', views.contact_create, name='contact_create'),
    path('contacts/<int:pk>/delete/', views.contact_delete, name='contact_delete'),
    
    # Leads
    path('leads/', views.leads_list, name='leads_list'),
    path('leads/add/', views.lead_create, name='lead_create'),
    path('leads/<int:pk>/edit/', views.lead_edit, name='lead_edit'),
    path('leads/<int:pk>/delete/', views.lead_delete, name='lead_delete'),
]