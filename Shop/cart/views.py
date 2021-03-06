from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from dress.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    """ Добавить товар в корзину """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    """ Удалить товар из корзины """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remuve(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    random_product = Product.objects.order_by('?')[:4]
    return render(request, 'cart/cart.html', {'cart': cart, 'random_product': random_product})

