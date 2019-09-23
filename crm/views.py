from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Company, Contact,ContactDetails, Quarry
#from bootstrap_datepicker_plus import DateTimePickerInput


# Company
class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'crm/company.html'
    context_object_name = 'companies'
    ordering = ['-pk']
class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company
class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    fields = ['company', 'field', 'remarks', 'address','area','city','country', 'website', 'phone', 'pending']
class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    fields = ['company', 'field', 'remarks', 'address','area','city','country', 'website', 'phone', 'pending']
class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    success_url = '/'

#Contact
class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'crm/contact.html'
    context_object_name = 'contacts'
    ordering = ['-pk']
class ContactDetailView(LoginRequiredMixin, DetailView):
    model = Contact
class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['date', 'company', 'comments','reminder']
    #to pass in the user foreign key
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class ContactUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Contact
    fields = ['date', 'company', 'comments','reminder']
    #LoginRequiredMixin:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.user:
            return True
        else:
            return False
class ContactDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model=Contact
    success_url = '/'
    def test_func(self):
        contact = self.get_object()
        if contact.user == self.request.user:
            return True
        else:
            return False

#Quarry
class QuarryListView(LoginRequiredMixin, ListView):
    model = Quarry
    template_name = 'crm/quarry.html'
    context_object_name = 'quarries'
    ordering = ['-pk']
class QuarryDetailView(LoginRequiredMixin, DetailView):
    model = Quarry
class QuarryCreateView(LoginRequiredMixin, CreateView):
    model = Quarry
    fields = ['company', 'area', 'country', 'name', 'type', 'colorPrimary', 'colorSecondary']
    # LoginRequiredMixin:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class QuarryUpdateView(LoginRequiredMixin, UpdateView):
    model = Quarry
    fields = ['company', 'area', 'country', 'name', 'type', 'colorPrimary', 'colorSecondary']
    #LoginRequiredMixin:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class QuarryDeleteView(LoginRequiredMixin, DeleteView):
    model=Quarry
    success_url = '/quarry/'
    def test_func(self):
        contact = self.get_object()
        if contact.user == self.request.user:
            return True
        else:
            return False


#Details / Personnel
@login_required
def person(request):
    context = {
        'contact_details' : ContactDetails.objects.all()
    }
    return  render(request, 'crm/contact_detail.html', context)

