from django.urls import path
from .views import profile, user_login, user_register, MyPasswordChange, MyPasswordReset, MyPasswordResetConfirm
from django.contrib.auth import views as auth_views
app_name = 'account'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('profile/', profile, name='profile'),
    path('password/', MyPasswordChange.as_view(), name='password'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', MyPasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', MyPasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]