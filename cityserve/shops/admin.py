from django.contrib import admin
from .models import Shop

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'city', 'contact')
    search_fields = ('name', 'category', 'address')
# Register your models here.
