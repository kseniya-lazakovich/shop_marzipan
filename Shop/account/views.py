from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required



@login_required
def profile(request):
    return render(request, 'account/profile.html')
