from django.contrib import admin
from django.urls import path
from domains import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.DomainListView.as_view(), name='domains'),
    path(
        'domain/<int:pk>/',
        views.DomainDetailView.as_view(),
        name='domain-detail'
    ),
]
