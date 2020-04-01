from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Category

def index(request):
    ctgs = Category.objects.all()
    return render(request, 'index.html', context={'ctgs': ctgs})
