from django.urls import path
from . import views

urlpatterns = [
    path('register/seller/',views.seller_register,name="seller_register"),
    path('register/customer/',views.customer_register, name="customer_register"),
]
