from django.urls import path
from .views import order_created

app_name = 'orders'

urlpatterns = [
    path('create/', order_created, name='order'),
]
