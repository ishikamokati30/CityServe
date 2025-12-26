from django.db import models
from shops.models import Shop

class Service(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    same_day_delivery = models.BooleanField(default=False)

    def __str__(self):
        return self.name
# Create your models here.
