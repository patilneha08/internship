from django.db import models
from django import forms

class Event(models.Model):
    name=models.CharField(max_length=64, default="")
    category=models.CharField(max_length=64, default="")
    maxpeople=models.CharField(max_length=64, default="")
    date=models.DateTimeField(max_length=64, default="")
    duration=models.DurationField(max_length=64, default="")
    location1=models.CharField(max_length=64, default="")
    location2=models.CharField(max_length=64, default="")
    city=models.CharField(max_length=64, default="")
    state=models.CharField(max_length=64, default="")
    pincode=models.IntegerField(default="")
    description=models.CharField(max_length=1000, default="")
    def __str__(self):
        return f"{self.name}     {self.category}     {self.date}"

class Eventcategory(models.Model):
    genre=models.CharField(max_length=64, default="")
    def __str__(self):
        return f"{self.genre}"

class Customer(models.Model):
    first_name=models.CharField(max_length=64, default="")
    last_name=models.CharField(max_length=64, default="")
    phone=models.BigIntegerField()
    username=models.EmailField(max_length=64, default="")
    password1=models.CharField(max_length=20, default="")
    password2=models.CharField(max_length=64, default="")
    def __str__(self):
        return f"{self.first_name} {self.last_name}   {self.username}"


class Eventmanager(models.Model):
    first_name=models.CharField(max_length=64, default="")
    last_name=models.CharField(max_length=64, default="")
    phone=models.BigIntegerField()
    username=models.EmailField(max_length=64, default="")
    password1=models.CharField(max_length=64, default="")
    password2=models.CharField(max_length=64, default="")
    def __str__(self):
        return f"{self.first_name} {self.last_name}     {self.username}"

