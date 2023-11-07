from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from product.forms import ProductForm, CartItemForm, ProductUpdateForm
from product.models import Product, CartItem


class ProductCreateView(SuccessMessageMixin, CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('list-of-products')
    success_message = '{l_name} {f_name}'

    # def get_success_message(self, cleaned_data):
    #     message = self.success_message + ' ' + 'is added successfully.'
    #     return message.format(f_name=self.object.product_name, l_name=self.object.color)
    #
    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_product = form.save(commit=False)
    #         new_product.product_name = new_product.first_name.title()
    #         new_product.color = new_product.color.title()
    #         new_product.save()
    #     return redirect('login')


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


class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'product/products_in_cards.html'
    model = Product
    context_object_name = 'all_products'
    # permission_required = 'product.view_list_of_products'

    def get_queryset(self):
        return Product.objects.filter()


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'product/delete_product.html'
    model = Product
    success_url = reverse_lazy('products-in-cards')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'product/update_product.html'
    model = Product
    form_class = ProductUpdateForm
    success_url = reverse_lazy('products-in-cards')
    # permission_required = 'seller.change_seller'

