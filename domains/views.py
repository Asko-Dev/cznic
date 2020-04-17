from datetime import datetime
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Domain, DomainFlag


# List view for all the domains registered
class DomainListView(ListView):
    """Lists all Domains"""
    model = Domain
    queryset = Domain.objects.all()
    template_name = 'domains.html'
    context_object_name = 'domains'
    ordering = ['date_created']


# List view for only existing (not deleted) domains
class ExistingDomainListView(DomainListView):
    """Lists existing Domains"""
    template_name = 'existing-domains.html'

    def get_queryset(self):
        return self.queryset.filter(date_deletion__gte=datetime.now())


# List view for only expired domains
class ExpiredDomainListView(DomainListView):
    """Lists existing Domains"""
    template_name = 'expired-domains.html'

    def get_queryset(self):
        return self.queryset.filter(date_deletion__lt=datetime.now())


# Detail List view for all the domains
class DomainDetailView(DetailView):
    """Lists detail data of a Domain"""
    model = Domain
    template_name = 'domains-detail.html'
    ordering = ['date_created']


# Don't ask
def EelOnMusk(request):
    """Because why not"""
    return render(request, 'eelonmusk.html', {'title': 'Because why not'})
