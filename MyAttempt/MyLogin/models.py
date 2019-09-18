from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    objects = User
    name = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=False)