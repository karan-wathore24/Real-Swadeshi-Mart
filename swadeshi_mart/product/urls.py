from django.urls import path
from .views import seller_dashboard, add_product

urlpatterns = [
    path('dashboard/', seller_dashboard, name='seller_dashboard'),
    # path('add-product/', add_product, name='add_product'),
]
