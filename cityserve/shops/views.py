from django.shortcuts import render, get_object_or_404
from .models import Shop
from services.models import Service
from products.models import Product
from django.db.models import Q


def shops_by_city(request, city_id):
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category')

    shops = Shop.objects.filter(city_id=city_id)

    if query:
        shops = shops.filter(
            Q(name__icontains=query) | Q(category__icontains=query)
        )

    if category:
        shops = shops.filter(category=category)

    return render(request, 'shops.html', {
        'shops': shops,
        'city_id': city_id
    })


def shop_detail(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)

    services = Service.objects.filter(shop=shop)

    # If Product has ForeignKey(shop, related_name="products")
    products = shop.products.all()

    return render(request, 'shop_detail.html', {
        'shop': shop,
        'services': services,
        'products': products
    })


# Create your views here.
