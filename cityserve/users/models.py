from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('USER', 'User'),
        ('SHOP', 'Shop Owner'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username
# Create your models here.
