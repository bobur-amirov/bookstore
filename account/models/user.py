from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    bio = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    img = models.ImageField(upload_to='users/', blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.username
