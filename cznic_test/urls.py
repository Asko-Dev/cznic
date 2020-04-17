from django.contrib import admin
from django.urls import path, include
from domains import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('domains.urls')),
]
