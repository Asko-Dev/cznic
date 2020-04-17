from django.utils import timezone
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
        return self.queryset.filter(date_deletion__gte=timezone.now())


# List view for only deleted domains
class DeletedDomainListView(DomainListView):
    """Lists existing Domains"""
    template_name = 'deleted-domains.html'

    def get_queryset(self):
        return self.queryset.filter(date_deletion__lt=timezone.now())


# Detail List view for the domains + context update for testing
class DomainDetailView(DetailView):
    """Lists detail data of a Domain"""
    model = Domain
    template_name = 'domains-detail.html'
    ordering = ['date_created']

    def get_context_data(self, **kwargs):
        context = super(DomainDetailView, self).get_context_data(**kwargs)
        context.update({
            'FQDN': self.object.FQDN,
            'date_created': self.object.date_created,
            'date_expires': self.object.date_expires,
            'date_deletion': self.object.date_deletion,
            'flags': self.object.flag.all()
        })
        return context


# Don't ask
def EelOnMusk(request):
    """Because why not"""
    return render(request, 'eelonmusk.html', {'title': 'Because why not'})
