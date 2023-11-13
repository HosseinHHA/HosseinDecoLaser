from django.urls import path

from product import views

urlpatterns = [
    path('create_product/', views.ProductCreateView.as_view(), name='create-product'),
    path('products_in_cards/', views.ProductListView.as_view(), name="products-in-cards"),
    path('delete_product/<int:pk>/', views.ProductDeleteView.as_view(), name="delete-product"),
    path('update_product/<int:pk>/', views.ProductUpdateView.as_view(), name="update-product"),
    path('search/', views.search, name="search"),
]
