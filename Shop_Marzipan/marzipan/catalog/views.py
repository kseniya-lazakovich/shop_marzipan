from django.shortcuts import render
from .models import Category, Catalog
from django.template.loader import get_template

# Create your views here.

def ctl(request):
    items = Catalog.objects.all()
    return render(request, 'catalog/catalog.html', context={'items':items})
