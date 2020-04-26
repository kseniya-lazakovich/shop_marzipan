from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Пароль'}))


class UserRegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Пароль *'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Повторите пароль *'}))
 

    class Meta:        
        model = User        
        fields = ('first_name', 'last_name', 'username', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Имя *'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Фамилия'}),
            'username' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Логин *'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-Mail *'}),      
        }
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']
