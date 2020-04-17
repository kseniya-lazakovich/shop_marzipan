from django.shortcuts import render, get_object_or_404 
from .models import Category, Product

def product_list(request, category_slug=None):    
    category = None    
    categories = Category.objects.all()    
    products = Product.objects.filter(available=True)    
    if category_slug:        
        category = get_object_or_404(Category, slug=category_slug)        
        products = products.filter(category=category)    
    return render(request, 'dress/shop.html', {'category': category, 'categories': categories, 'products': products})

def product_detail(request, id, slug):    
    product = get_object_or_404(Product, id=id, slug=slug, available=True)    
    return render(request, 'dress/product-single.html', {'product': product})

def index(request):    
    random_product = Product.objects.order_by('?')[:4]
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    return render(request, 'dress/index.html', {'categories': categories, 'products': products, 'random_product': random_product,})