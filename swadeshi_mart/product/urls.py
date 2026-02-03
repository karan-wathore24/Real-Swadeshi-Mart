from django.urls import path
from .views import shop, product_detail

urlpatterns = [
    path('', shop, name='home'),
    path('product/<int:id>/', product_detail, name='product_detail'),
]
