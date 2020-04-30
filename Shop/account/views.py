from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .forms import UserRegForm
from django.contrib import messages
from django.views.generic.edit import FormView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


@login_required
def profile(request):
    """страница профиля"""
    return render(request, 'account/profile.html')

class PasswordChange(PasswordChangeView, SuccessMessageMixin, LoginRequiredMixin):
    """ Смена пароля """
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('account:password')
    success_message = 'Пароль пользователя изменен'

    
class AccountView(TemplateView):
    """ Обработка get запроса """
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        login_form = LoginForm(self.request.GET or None)
        user_form = UserRegForm(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['login_form'] = login_form
        context['user_form'] = user_form
        return self.render_to_response(context)


class LoginFormView(FormView):
    """ обработка формы входа """
    form_class = LoginForm
    template_name = 'account/profile.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        login_form = self.form_class(request.POST)
        user_form = UserRegForm()
        if login_form.is_valid():
            cd = login_form.cleaned_data
            # authenticate() сверяет данные с БД
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                # login() запоминает пользователя в сессии
                    login(request, user)
                    return render(request, 'account/profile.html')
                else:
                    return render(request, 'registration/logged_out.html')
            else:
                messages.error(request, 'Неправильный логин или пароль')
            return self.render_to_response(
                self.get_context_data(
                success=True
            )
        )
        else:
            login_form = LoginForm()
            return self.render_to_response(self.get_context_data(login_form=login_form, user_form=user_form,))

class UserRegFormView(FormView):
    """ обработка формы регистрации """
    form_class = UserRegForm
    template_name = 'registration/success.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        user_form = self.form_class(request.POST)
        login_form = LoginForm()
        if user_form.is_valid():
            new_user = user_form.save(commit=False) #создаем нового польз
            new_user.set_password(user_form.cleaned_data['password']) #задаем зашифров пароль
            new_user.save() #сохраняем польз
            return self.render_to_response(
                self.get_context_data(success=True))
        else:
            user_form = UserRegForm()
            return self.render_to_response(self.get_context_data(user_form=user_form, login_form=login_form))
