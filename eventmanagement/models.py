from django.db import models

class User(models.Model):
    First_name=models.CharField(max_length=64, default="")
    Last_name=models.CharField(max_length=64, default="")
    phone=models.BigIntegerField()
    username=models.EmailField(max_length=64, default="")
    password=models.CharField(max_length=64, default="")
    def __str__(self):
        return f"{self.First_name}"


class Eventmanager(models.Model):
    First_name=models.CharField(max_length=64, default="")
    Last_name=models.CharField(max_length=64, default="")
    phone=models.BigIntegerField()
    username=models.EmailField(max_length=64, default="")
    password=models.CharField(max_length=64, default="")
    def __str__(self):
        return f"{self.First_name}"

