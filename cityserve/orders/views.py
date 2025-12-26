from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import CartItem, Order, OrderItem, Coupon
from decimal import Decimal


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    subtotal = sum(item.total_price for item in cart_items)

    discount = Decimal('0')
    coupon_code = request.GET.get('coupon')

    if coupon_code:
        try:
            coupon = Coupon.objects.get(code=coupon_code, active=True)
            discount = subtotal * Decimal(coupon.discount_percent) / Decimal('100')
        except Coupon.DoesNotExist:
            pass

    delivery_charge = Decimal('50') if subtotal < 500 and subtotal > 0 else Decimal('0')
    total = subtotal - discount + delivery_charge

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'discount': discount,
        'delivery_charge': delivery_charge,
        'total': total,
        'coupon_code': coupon_code
    })


@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        return redirect('cart')

    subtotal = sum(item.total_price for item in cart_items)

    coupon_code = request.GET.get('coupon')
    discount = Decimal('0')
    if coupon_code:
        try:
            coupon = Coupon.objects.get(code=coupon_code, active=True)
            discount = subtotal * Decimal(coupon.discount_percent) / Decimal('100')
        except Coupon.DoesNotExist:
            pass

    delivery_charge = Decimal('50') if subtotal < 500 and subtotal > 0 else Decimal('0')
    total = subtotal - discount + delivery_charge

    if request.method == 'POST':
        delivery = request.POST.get('delivery_option')
        payment = request.POST.get('payment_mode')

        order = Order.objects.create(
            user=request.user,
            subtotal=subtotal,
            discount=discount,
            delivery_charge=delivery_charge,
            total=total,
            delivery_option=delivery,
            payment_mode=payment
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )

        cart_items.delete()
        return redirect('order_success')

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'discount': discount,
        'delivery_charge': delivery_charge,
        'total': total,
        'coupon_code': coupon_code
    })


@login_required
def order_success(request):
    return render(request, 'order_success.html')


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart')


@login_required
def update_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if request.method == "POST":
        qty = int(request.POST.get('quantity'))
        if qty > 0:
            item.quantity = qty
            item.save()
        else:
            item.delete()
    return redirect('cart')

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_detail.html', {'order': order})