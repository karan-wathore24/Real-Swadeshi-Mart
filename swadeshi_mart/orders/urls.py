from django.urls import path
from . import views

urlpatterns = [
    path('place/', views.place_order, name='place_order'),
    path('detail/<int:id>/', views.order_detail, name='order_detail'),

]
