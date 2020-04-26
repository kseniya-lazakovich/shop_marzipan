from .cart import Cart
from dress.models import Category


def cart(request):
    return {'cart': Cart(request)}

def ctg(request):
    categories = Category.objects.all()
    return {'categories':categories}
