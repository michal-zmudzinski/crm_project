from django.db import models
from django.utils import timezone
# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=75)
    surname = models.CharField(max_length=125)
    dateOfBirth = models.DateField(default=timezone.now)
    login = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=32)
    isDeleted = models.BooleanField(default=False)
