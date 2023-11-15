from django.urls import path

from userextend import views
from .views import user_logout

urlpatterns = [
    path('create_user/', views.UserCreateView.as_view(), name='create-user'),
    path('logout/', user_logout, name='logout'),
]

