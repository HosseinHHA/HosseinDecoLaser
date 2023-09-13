from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from product.forms import ProductForm
from product.models import Product


# Create your views here.

class ProductCreateView(SuccessMessageMixin, CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('home-page')
    success_message = '{f_name} {l_name}'

