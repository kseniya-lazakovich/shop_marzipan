from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from .models import Category, Product
from django.views.generic.base import TemplateView
from cart.forms import CartAddProductForm


''' Товары и категории '''


def index(request):
    random_product = Product.objects.order_by('?')[:4]
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'dress/index.html', {'categories': categories, 'products': products, 'random_product': random_product, })

def about(request):
    categories = Category.objects.all()
    return render(request, 'dress/about.html', {'categories': categories})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'dress/product/product-list.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm() 
    return render(request, 'dress/product/product-detail.html', {'product': product, 'cart_product_form':cart_product_form})


''' Авторизация '''

def login(request):
    categories = Category.objects.all()
    return render(request, 'dress/checkout.html', {'categories': categories})


# from django.contrib.auth import authenticate, login
# from .forms import LoginForm

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'],
#                                 password = cd['password'])
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponse('Вход выполнен')
#             else:
#                 return HttpResponse('Вы вышли')
#         else:
#             return HttpResponse('Неправильный логин или пароль')
#     else:
#         form = LoginForm()
#     return render(request, 'dress/account/checkout.html', {'form': form})