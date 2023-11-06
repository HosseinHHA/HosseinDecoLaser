from django.urls import path

from seller import views

urlpatterns = [
    path('create_seller/', views.SellerCreateView.as_view(), name='create-seller'),
    path('list_of_sellers/', views.SellerListView.as_view(), name="list-of-sellers"),
    path('delete_seller/<int:pk>/', views.SellerDeleteView.as_view(), name="delete-seller"),
    path('update_seller/<int:pk>/', views.SellerUpdateView.as_view(), name="update-seller"),
]
