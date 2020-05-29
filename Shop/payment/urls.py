from django.urls import path
from .views import payment_process, payment_done, payment_canceled

app_name = 'payment'

urlpatterns = [
    path('process/', payment_process, name='process'),
    path('done/', payment_done, name='done'),
    path('canceled/', payment_canceled, name='canceled'),
]