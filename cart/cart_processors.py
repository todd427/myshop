from .cart import Cart
from django.conf import settings

def cart(request):
    return {'cart': Cart(request)}

def get_cart_total(request):
    cart = Cart(request)
    return cart.get_total_price()


