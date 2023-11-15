from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from product.forms import ProductForm, ProductUpdateForm
from product.models import Product


class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products-in-cards')
    success_message = '{l_name} {f_name}'


class ProductListView(ListView):
    template_name = 'product/products_in_cards.html'
    model = Product
    context_object_name = 'all_products'

    def get_queryset(self):
        return Product.objects.filter()


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'product/delete_product.html'
    model = Product
    success_url = reverse_lazy('products-in-cards')
    permission_required = 'seller.delete_seller'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'product/update_product.html'
    model = Product
    form_class = ProductUpdateForm
    success_url = reverse_lazy('products-in-cards')


def search(request):
    get_value = request.GET.get('filter')
    if get_value:
        product = Product.objects.filter(Q(product_name__icontains=get_value) | Q(color__icontains=get_value))
    else:
        product = Product.objects.all()

    return render(request, 'product/products_in_cards.html', {'all_products': product})

