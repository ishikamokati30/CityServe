from django.db import models
from shops.models import Shop

class Product(models.Model):
    shop = models.ForeignKey(
    Shop,
    on_delete=models.CASCADE,
    related_name="products",
    default=1   # ← use the shop ID you created
)

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.IntegerField(default=0)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    @property
    def discounted_price(self):
        if self.discount_percent > 0:
            return self.price * (100 - self.discount_percent) / 100
        return self.price

    def __str__(self):
        return self.name
# Create your models here.
