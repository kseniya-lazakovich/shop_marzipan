from django.urls import path
from .views import user_login
app_name = 'account'

urlpatterns = [
    path('login/', user_login, name='login'),
]