from django.contrib import admin
from django.urls import path
from domains import views

app_name = ''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.DomainListView.as_view(), name='all-domains'),
    path(
        'existing/',
        views.ExistingDomainListView.as_view(),
        name='existing-domains'
    ),
    path(
        'deleted/',
        views.DeletedDomainListView.as_view(),
        name='deleted-domains'
    ),
    path(
        'domain/<int:pk>/',
        views.DomainDetailView.as_view(),
        name='domain-detail'
    ),
    path('why-not/', views.EelOnMusk, name='why-not'),
]
