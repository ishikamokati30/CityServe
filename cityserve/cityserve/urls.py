"""
URL configuration for cityserve project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cities.views import city_list
from django.conf import settings
from django.conf.urls.static import static
from shops.views import shops_by_city, shop_detail
from orders.views import (
    add_to_cart,
    checkout,
    cart_view,
    order_success,
    remove_from_cart,
    update_quantity,
    order_list,
    order_detail,
)
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', city_list, name='cities'),

    path('shops/<int:city_id>/', shops_by_city, name='shops'),
    path('shop/<int:shop_id>/', shop_detail, name='shop_detail'),

    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('order-success/', order_success, name='order_success'),

    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update-quantity/<int:item_id>/', update_quantity, name='update_quantity'),

    path('orders/', order_list, name='orders'),
    path('orders/<int:order_id>/', order_detail, name='order_detail'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
