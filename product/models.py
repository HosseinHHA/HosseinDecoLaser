from django.db import models

from seller.models import Seller


class Product(models.Model):
    product_name = models.CharField(max_length=70)
    color = models.CharField(max_length=30)
    description = models.TextField(max_length=700)
    image = models.ImageField(upload_to='product_image/', null=True)
    price = models.IntegerField()
    # seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product_name} {self.color}'


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

