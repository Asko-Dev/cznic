from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Domain, DomainFlag


# List view for all the Domains registered
class DomainListView(ListView):
    """Lists all Domains"""
    model = Domain
    template_name = 'domains.html'
    context_object_name = 'domains'
    ordering = ['date_created']


class DomainDetailView(DetailView):
    """Lists detail data of a Domain"""
    model = Domain
    template_name = 'domains-detail.html'
    ordering = ['date_created']
