from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.seller_dashboard, name='seller_dashboard'),
    # path('add-product/', add_product, name='add_product'),
    path('product/<int:pk>/',views.product_detail,name='product_detail'),
]
