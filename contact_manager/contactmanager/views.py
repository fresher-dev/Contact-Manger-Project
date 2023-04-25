from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Contact
from .forms import ContactForm
from django.db.models import Q
import csv


class HomeBaseView(TemplateView):
    template_name = "contactmanager/index.html"


class AddContactView(CreateView):
    form_class = ContactForm
    success_url = reverse_lazy("contact_manager:home")
    template_name = "contactmanager/add_contact.html"


class AllContactView(ListView):
    template_name = "contactmanager/all_contact.html"
    model = Contact
    context_object_name = 'contacts'


class EditContactView(UpdateView):
    template_name = "contactmanager/edit_contact.html"
    model = Contact
    fields = ["name", "email", "phone"]


class DeleteContactView(DeleteView):
    template_name = "contactmanager/delete_contact.html"
    model = Contact
    success_url = reverse_lazy("contact_manager:all")


def search(request):
    if request.method == "GET":
        query = request.GET.get('q')
        if query is not None:
            results = Contact.objects.filter(Q(name__icontains=query) \
                                             or Q(phone__icontains=query) or Q(email__contains=query))
            return render(request, "contactmanager/search.html", {
                "results": results,
            })
    return render(request, "contactmanager/search.html")


def export(request):
    data_dict = Contact.objects.values()
    with open("contact_manager.csv", mode='w') as csv_file:
        fieldnames = ['id', 'name', 'phone', 'email']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for i in data_dict:
            writer.writerow(i)
    return redirect("contact_manager:home")
