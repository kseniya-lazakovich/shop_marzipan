from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'country', 'city',
                  'address', 'postal_code']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control  ', 'placeholder': 'Имя *'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control  ', 'placeholder': 'Фамилия *'}),
            'country': forms.TextInput(attrs={'class': 'form-control  ', 'placeholder': 'Страна *'}),
            'email': forms.TextInput(attrs={'class': 'form-control  ', 'placeholder': 'E-Mail *'}),
            'city': forms.TextInput(attrs={'class': 'form-control  ', 'placeholder': 'Город *'}),
            'address': forms.TextInput(attrs={'class': 'form-control  ', 'placeholder': 'Адрес *'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control  ', 'placeholder': 'Индекс *'}),
        }
