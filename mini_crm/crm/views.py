from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.db.models import Count, Q
from .models import Contact, Lead
from .forms import ContactForm, LeadForm

@login_required
def dashboard(request):
    contacts_count = Contact.objects.filter(created_by=request.user).count()
    leads_count = Lead.objects.filter(created_by=request.user).count()
    
    recent_contacts = Contact.objects.filter(created_by=request.user)[:5]
    recent_leads = Lead.objects.filter(created_by=request.user)[:5]
    
    # Lead status breakdown
    lead_stats = Lead.objects.filter(created_by=request.user).values('status').annotate(count=Count('status'))
    
    context = {
        'contacts_count': contacts_count,
        'leads_count': leads_count,
        'recent_contacts': recent_contacts,
        'recent_leads': recent_leads,
        'lead_stats': lead_stats,
    }
    return render(request, 'crm/dashboard.html', context)

@login_required
def contacts_list(request):
    contacts = Contact.objects.filter(created_by=request.user)
    return render(request, 'crm/contacts.html', {'contacts': contacts})

@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.created_by = request.user
            contact.save()
            messages.success(request, 'Contact created successfully!')
            return redirect('contacts_list')
    else:
        form = ContactForm()
    return render(request, 'crm/contact_form.html', {'form': form, 'title': 'Add Contact'})

@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk, created_by=request.user)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact deleted successfully!')
        return redirect('contacts_list')
    return render(request, 'crm/contact_confirm_delete.html', {'contact': contact})

@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by=request.user)
    return render(request, 'crm/leads.html', {'leads': leads})

@login_required
def lead_create(request):
    if request.method == 'POST':
        form = LeadForm(request.user, request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            messages.success(request, 'Lead created successfully!')
            return redirect('leads_list')
    else:
        form = LeadForm(request.user)
    return render(request, 'crm/lead_form.html', {'form': form, 'title': 'Add Lead'})

@login_required
def lead_edit(request, pk):
    lead = get_object_or_404(Lead, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = LeadForm(request.user, request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lead updated successfully!')
            return redirect('leads_list')
    else:
        form = LeadForm(request.user, instance=lead)
    return render(request, 'crm/lead_form.html', {'form': form, 'title': 'Edit Lead'})

@login_required
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk, created_by=request.user)
    if request.method == 'POST':
        lead.delete()
        messages.success(request, 'Lead deleted successfully!')
        return redirect('leads_list')
    return render(request, 'crm/lead_confirm_delete.html', {'lead': lead})

def custom_logout(request):
    logout(request)
    return redirect('login')