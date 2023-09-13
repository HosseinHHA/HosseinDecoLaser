from django.urls import path

from product import views

urlpatterns = [
    path('create_product/', views.ProductCreateView.as_view(), name='create-product'),
]