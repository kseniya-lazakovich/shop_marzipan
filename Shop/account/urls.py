from django.urls import path
from .views import profile, user_login
from django.contrib.auth import views as auth_views
app_name = 'account'

urlpatterns = [
    # path('', AccountView.as_view(), name='auth'),
    path('login/', user_login, name='login'),
    # path('register/', UserRegFormView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    # path('password/', PasswordChange.as_view(), name='password'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    
]