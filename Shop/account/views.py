from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .forms import UserRegForm
from django.views.generic.edit import FormView


# def _get_form(request, formcls, prefix):
#     data = request.POST if prefix in request.POST else None
#     return formcls(data, prefix=prefix)


# class AccountView(TemplateView):
#     template_name = 'registration/login.html'

#     def get(self, request, *args, **kwargs):
#         return self.render_to_response({'login_form': LoginForm(prefix='login_pre'), 'user_form': UserRegForm(prefix='user_pre')})

#     def post(self, request, *args, **kwargs):
#         login_form = _get_form(request, LoginForm, 'login_pre')
#         user_form = _get_form(request, UserRegForm, 'user_pre')
#         if login_form.is_valid():
#             def user_login(request):
#                 if request.method == 'POST':
#                     login_form = LoginForm(request.POST)
#                     user_form = UserRegForm()
#                     if login_form.is_valid():
#                         cd = login_form.cleaned_data
#                         # authenticate() сверяет данные с БД
#                         user = authenticate(request, username=cd['username'], password=cd['password'])
#                     if user is not None:
#                         if user.is_active:
#                             # login() запоминает пользователя в сессии
#                             login(request, user)
#                             return render(request, 'account/profile.html')
#                         else:
#                             return render(request, 'registration/logged_out.html')
#                     # else:
#                     #     return HttpResponse('Неправильный логин или пароль')
#                 else:
#                     login_form = LoginForm()
#                 return  render(request, 'registration/login.html', {'login_form': login_form})
#         elif user_form.is_bound and user_form.is_valid():
#             def register(request):
#                 if request.method == 'POST':
#                     user_form = UserRegForm(request.POST)
#                     login_form = LoginForm()
#                     if user_form.is_valid():
#                         new_user = user_form.save(commit=False) #создаем нового польз
#                         new_user.set_password(user_form.cleaned_data['password']) #задаем зашифров пароль
#                         new_user.save() #сохраняем польз
#                         return {'new_user':new_user}
#                 else:
#                     user_form = UserRegForm()
#                     return {'user_form': user_form}
#             return self.render_to_response({'login_form': login_form, 'user_form': user_form})

# # def user_login(request):
# #     if request.method == 'POST':
# #         login_form = LoginForm(request.POST)
# #         user_form = UserRegForm()
# #         if login_form.is_valid():
# #             cd = login_form.cleaned_data
# #             user = authenticate(request, username=cd['username'], password=cd['password']) #authenticate() сверяет данные с БД
# #         if user is not None:
# #             if user.is_active:
# #                 login(request, user) #login() запоминает пользователя в сессии
# #                 return render(request, 'account/profile.html')

# #             else:
# #                 return render(request, 'registration/logged_out.html')
# #         else:
# #             return HttpResponse('Неправильный логин или пароль')
# #     else:
# #         login_form = LoginForm()
# #     return {'login_form': login_form}

@login_required
def profile(request):
    return render(request,'account/profile.html')

# # def register(request):
# #     if request.method == 'POST':
# #         user_form = UserRegForm(request.POST)
# #         login_form = LoginForm()
# #         if user_form.is_valid():
# #             new_user = user_form.save(commit=False) #создаем нового польз
# #             new_user.set_password(user_form.cleaned_data['password']) #задаем зашифров пароль
# #             new_user.save() #сохраняем польз
# #             return {'new_user':new_user}
# #     else:
# #         user_form = UserRegForm()
# #     return {'user_form': user_form}

class AccountView(TemplateView):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        login_form = LoginForm(self.request.GET or None)
        user_form = UserRegForm(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['login_form'] = login_form
        context['user_form'] = user_form
        return self.render_to_response(context)


class LoginFormView(FormView):
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
                return HttpResponse('Неправильный логин или пароль')
            return self.render_to_response(
                self.get_context_data(
                success=True
            )
        )
        else:
            login_form = LoginForm()
            return self.render_to_response(self.get_context_data(login_form=login_form,))

class UserRegFormView(FormView):
    form_class = UserRegForm
    template_name = 'account/profile.html'
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
