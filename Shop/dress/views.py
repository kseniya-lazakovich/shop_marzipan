from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    random_product = Product.objects.order_by('?')[:4]
    products = Product.objects.all()
    return render(request, 'dress/index.html', {'products': products, 'random_product': random_product, })


def about(request):
    return render(request, 'dress/about.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    try:
        product_page = paginator.page(page)
    except PageNotAnInteger:
        product_page = paginator.page(1)
    except EmptyPage:
        product_page = paginator.page(paginator.num_pages)
    return render(request, 'dress/product/product-list.html', {'category': category, 'categories': categories, 'products': products, 'page': page, 'product_page': product_page})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'dress/product/product-detail.html', {'product': product, 'cart_product_form': cart_product_form})
