from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)