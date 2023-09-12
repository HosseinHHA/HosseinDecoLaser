from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from seller.forms import SellerForm
from seller.models import Seller


# Create your views here.

class SellerCreateView(SuccessMessageMixin, CreateView):
    template_name = 'seller/create_seller.html'
    model = Seller
    form_class = SellerForm
    success_url = reverse_lazy('home-page')
    success_message = '{f_name} {l_name}'

    def get_success_message(self, cleaned_data):
        message = self.success_message + ' ' + 'is added successfully.'
        return message.format(f_name=self.object.first_name, l_name=self.object.last_name)




