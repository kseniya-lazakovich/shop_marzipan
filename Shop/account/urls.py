from django.urls import path
from .views import profile, AccountView, LoginFormView, UserRegFormView
from django.contrib.auth import views as auth_views
app_name = 'account'

urlpatterns = [
    path('auth/', AccountView.as_view(), name='auth'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('register/', UserRegFormView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    
]