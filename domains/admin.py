from django.contrib import admin
from . import models


admin.site.register(models.Domain)
admin.site.register(models.DomainFlag)
