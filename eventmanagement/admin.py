from django.contrib import admin
from .models import Eventmanager, CustomUser

admin.site.register(CustomUser)
admin.site.register(Eventmanager)
