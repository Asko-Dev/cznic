from django.contrib import admin
from django.urls import path
from domains import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.DomainListView.as_view(), name='domains'),
    path(
        'existing/',
        views.ExistingDomainListView.as_view(),
        name='existing-domains'
    ),
    path(
        'expired/',
        views.ExpiredDomainListView.as_view(),
        name='expired-domains'
    ),
    path(
        'domain/<int:pk>/',
        views.DomainDetailView.as_view(),
        name='domain-detail'
    ),
    path('why-not/', views.EelOnMusk, name='why-not'),
]
