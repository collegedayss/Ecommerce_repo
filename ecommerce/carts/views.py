from django.shortcuts import render

from products.models import Product
from .models import Cart


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    print(
        f"cart id : {cart_obj} and cart product total is {total} and  queryset {cart_obj.products.all()}")
    cart_obj.total = total
    cart_obj.save()
    return render(request, "carts/home.html", {})
