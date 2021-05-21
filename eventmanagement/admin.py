from django.contrib import admin
from .models import Eventmanager, Customer, Event

admin.site.register(Customer)
admin.site.register(Eventmanager)
admin.site.register(Event)

