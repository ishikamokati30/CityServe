from django.db import models
from cities.models import City
from django.contrib.auth.models import User
from datetime import datetime

class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return self.name

    def is_open(self):
        current_time = datetime.now().time()
        return self.open_time <= current_time <= self.close_time

# Create your models here.
