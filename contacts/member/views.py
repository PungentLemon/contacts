from django.views.generic import (ListView, DetailView, CreateView,
                                    UpdateView, DeleteView)
from django.urls import reverse
from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

def index(request):
    return render(request,'member/index.html')

class ContactList(ListView):
    model = Contact

class ContactDetail(DetailView):
    model = Contact


class ContactCreate(CreateView):
    model = Contact
    fields= ['name','email','address','phone']
    def contact_detail(self,request):
        if request.method=="POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()

    def get_success_url(self):
         return reverse('contact_list')



class ContactUpdate(UpdateView):
    model = Contact
    fields = ['name','email','address','phone']
    template_name_suffix = '_update_form'
    def contact_detail(self,request):
        if request.method=="POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()

    def get_success_url(self):
         return reverse('contact_list')

class ContactDelete(DeleteView):
    model = Contact

    def get_success_url(self):
         return reverse('contact_list')
