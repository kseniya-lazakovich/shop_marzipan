from django.shortcuts import render
from django.views.generic.base import View

from .models import Item 

class ItemView(View):
    def get(self, request):
        items = Item.objects.all()
        return render(request, "index.html", {items: 'items'})
