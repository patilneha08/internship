from django.contrib import admin
from .models import Eventcategory, Eventmanager, Customer, Event

admin.site.register(Customer)
admin.site.register(Eventmanager)
admin.site.register(Event)
admin.site.register(Eventcategory)
