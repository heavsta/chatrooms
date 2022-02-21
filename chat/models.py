from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Room(models.Model):
    name = models.CharField(max_length=12)
    fullName = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.name}'