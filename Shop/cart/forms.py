from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label='', initial='1', widget=forms.TextInput(attrs={"class":"form-control input-number"}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
