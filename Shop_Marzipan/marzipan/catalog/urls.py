from django.urls import path
from .views import ctl

urlpatterns = [
    path('', ctl, name='catalog'),
]
