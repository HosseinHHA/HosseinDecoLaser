from django.urls import path

from seller import views

urlpatterns = [
    path('create_seller/', views.SellerCreateView.as_view(), name='create-seller'),
]