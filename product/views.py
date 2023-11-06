from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from product.forms import ProductForm, CartItemForm
from product.models import Product, CartItem


# Create your views here.

class ProductCreateView(SuccessMessageMixin, CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('home-page')
    success_message = '{f_name} {l_name}'


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.product = product
            cart_item.save()
            return redirect('cart')
    else:
        form = CartItemForm()
    return render(request, 'product/add_to_cart.html', {'form': form, 'product': product})


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    cart_item.delete()
    return redirect('cart')

