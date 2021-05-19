from django import forms
from .models import *

class HostEvent(forms.Form):
    name=forms.CharField(label="Name of Event", max_length=64)
    category=forms.CharField(label="Category", max_length=64)
    maxpeople=forms.CharField(label="Maximum number of Participants", max_length=64)
    date=forms.DateTimeField(label="Date and Time")
    duration=forms.DurationField(label="Duration")
    location1=forms.CharField(label="Street Address", max_length=64)
    location2=forms.CharField(label="Street Address Line 2", max_length=64)
    city=forms.CharField(label="City", max_length=64)
    state=forms.CharField(label="State/Province", max_length=64)
    pincode=forms.IntegerField(label="Postal/ Zip Code")
    description=forms.CharField(label="Description of the Event", max_length=1000)


# class Customerform(forms.Form):
#     first_name=forms.CharField(label='First Name', max_length=100)
#     last_name=forms.CharField(label='Last Name', max_length=100)
#     phone=forms.CharField(label='Contact Number', max_length=100)
#     username=forms.EmailField(label='Email Address or Username', max_length=100)
#     password1=forms.CharField(label='Enter Password', max_length=100)
#     password2=forms.CharField(label='Confirm Password', max_length=100)

# class Eventmanagerform(forms.Form):
#     first_name=forms.CharField(label='First Name', max_length=100)
#     last_name=forms.CharField(label='Last Name', max_length=100)
#     phone=forms.CharField(label='Contact Number', max_length=100)
#     username=forms.EmailField(label='Email Address or Username', max_length=100)
#     password1=forms.CharField(label='Enter Password', max_length=100)
#     password2=forms.CharField(label='Confirm Password', max_length=100)

