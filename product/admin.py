from django.contrib import admin

from product.models import Product
from seller.models import Seller

admin.site.register(Product)
admin.site.register(Seller)

