from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView

from seller.forms import SellerForm
from seller.models import Seller


# Create your views here.

class SellerCreateView(SuccessMessageMixin, CreateView):
    template_name = 'seller/create_seller.html'
    model = Seller
    form_class = SellerForm
    success_url = reverse_lazy('list-of-sellers')
    success_message = '{f_name} {l_name}'

    def get_success_message(self, cleaned_data):
        message = self.success_message + ' ' + 'is added successfully.'
        return message.format(f_name=self.object.first_name, l_name=self.object.last_name)
    
    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_seller = form.save(commit=False)
    #         new_seller.first_name = new_seller.first_name.title()
    #         new_seller.last_name = new_seller.last_name.title()
    #         new_seller.save()
    #     return redirect('login')


class SellerListView(ListView):
    template_name = 'seller/list_of_sellers.html'
    model = Seller
    context_object_name = 'all_sellers'  # Seller.object.all()
    # permission_required = 'seller.view_list_of_sellers'

    def get_queryset(self):
        return Seller.objects.filter(active=True)
    
    
# class SellerDeleteView(DeleteView):
#     template_name = 'seller/delete_seller.html'
#     model = Seller
#     success_url = reverse_lazy('list-of-sellers')


