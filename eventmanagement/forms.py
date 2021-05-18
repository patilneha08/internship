from django import forms

class Customerform(forms.Form):
    first_name=forms.CharField(label='First Name', max_length=100)
    last_name=forms.CharField(label='Last Name', max_length=100)
    phone=forms.CharField(label='Contact Number', max_length=100)
    username=forms.EmailField(label='Email Address or Username', max_length=100)
    password=forms.CharField(label='Enter Password', max_length=100)
    password1=forms.CharField(label='Confirm Password', max_length=100)

class Eventmanagerform(forms.Form):
    first_name=forms.CharField(label='First Name', max_length=100)
    last_name=forms.CharField(label='Last Name', max_length=100)
    phone=forms.CharField(label='Contact Number', max_length=100)
    username=forms.EmailField(label='Email Address or Username', max_length=100)
    password=forms.CharField(label='Enter Password', max_length=100)
    password1=forms.CharField(label='Confirm Password', max_length=100)