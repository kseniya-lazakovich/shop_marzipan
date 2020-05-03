from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from .models import Profile
from .forms import LoginForm, UserRegForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваши данные успешно изменены')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/profile.html', {'user_form': user_form, 'profile_form': profile_form})


class MyPasswordChange(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    """ Смена пароля """
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('account:password')
    success_message = 'Ваш пароль успешно изменён'


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'dress/index.html')
            else:
                return render(request, 'registration/logget_out.html')
        else:
            messages.warning(request, 'Неверный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegForm(request.POST)
        if user_form.is_valid():
            # Создаем нового пользователя, но пока не сохраняем в базу данных.
            new_user = user_form.save(commit=False)
            # # Задаем пользователю зашифрованный пароль.
            new_user.set_password(user_form.cleaned_data['password'])
            Profile.objects.create(user=new_user)
            # Сохраняем пользователя в базе данных.
            new_user.save()
            return render(request, 'registration/success.html', {'new_user': new_user})
    else:
        user_form = UserRegForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


