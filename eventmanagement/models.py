from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=64, default="")
    last_name=models.CharField(max_length=64, default="")
    phone=models.BigIntegerField()
    username=models.EmailField(max_length=64, default="")
    password=models.CharField(max_length=64, default="")
    password1=models.CharField(max_length=64, default="")
    def __str__(self):
        return f"{self.first_name} {self.last_name}     {self.username}"


class Eventmanager(models.Model):
    first_name=models.CharField(max_length=64, default="")
    last_name=models.CharField(max_length=64, default="")
    phone=models.BigIntegerField()
    username=models.EmailField(max_length=64, default="")
    password=models.CharField(max_length=64, default="")
    password1=models.CharField(max_length=64, default="")
    def __str__(self):
        return f"{self.first_name} {self.last_name}     {self.username}"

