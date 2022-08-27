from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.authtoken.models import Token


class Users(AbstractUser):
    address = models.CharField(max_length=30, blank=True)
  
