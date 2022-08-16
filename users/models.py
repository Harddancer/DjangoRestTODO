from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    address = models.CharField(max_length=30, blank=True)
    name_user = models.CharField(max_length=64)
    
class Project(models.Model):
    name_project = models.CharField(max_length=64)
    user = models.ManyToManyField(Users)

class TODO(models.Model):
    name_todo = models.CharField(max_length=64)
    text = models.CharField(max_length=64)
    date_creation = models.DateField
    date_update = models.DateField
    name_user = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
    user = models.OneToOneField(Users, on_delete=models.CASCADE)