from django.urls import path
from .views import profile, user_login, user_register, MyPasswordChange
from django.contrib.auth import views as auth_views
app_name = 'account'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('profile/', profile, name='profile'),
    path('password/', MyPasswordChange.as_view(), name='password'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]