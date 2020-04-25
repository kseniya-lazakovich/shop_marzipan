from django.urls import path
from .views import profile
from django.contrib.auth import views as auth_views
app_name = 'account'

urlpatterns = [
    # path('login/', user_login, name='login'),
    path('', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
]