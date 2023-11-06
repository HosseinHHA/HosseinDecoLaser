from django import forms
from django.forms import TextInput, Textarea, NumberInput

from product.models import Product, CartItem


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'product_name', 'color', 'description', 'price', 'image']
        widgets = {
            'product_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the product name'}),
            'color': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter color of the product'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter form, size '
                                                                    'and material of the product', 'rows': 4}),
            'price': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
        }


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

