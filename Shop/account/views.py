from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password']) #authenticate() сверяет данные с БД
        if user is not None:
            if user.is_active:
                login(request, user) #login() запоминает пользователя в сессии
                return HttpResponse('Вход выполнен')
            else:
                return HttpResponse('Вы вышли')
        else:
            return HttpResponse('Неправильный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'account/checkout.html', {'form': form})
