from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from .models import Category, Product
from django.views.generic.base import TemplateView
from cart.forms import CartAddProductForm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


''' Товары и категории '''


def index(request):
    random_product = Product.objects.order_by('?')[:4]
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'dress/index.html', {'categories': categories, 'products': products, 'random_product': random_product, })


def about(request):
    categories = Category.objects.all()
    return render(request, 'dress/about.html', {'categories': categories})


def news(request):
    return render(request, 'dress/news.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    try:
        product_page = paginator.page(page)
    except PageNotAnInteger:
        product_page = paginator.page(1)
    except EmptyPage:
        product_page = paginator.page(paginator.num_pages)
    return render(request, 'dress/product/product-list.html', {'category': category, 'categories': categories, 'products': products, 'page':page, 'product_page':product_page})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'dress/product/product-detail.html', {'product': product, 'cart_product_form': cart_product_form})
