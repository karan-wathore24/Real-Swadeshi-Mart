from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name="home"),
    path('register/seller/',views.seller_register,name="seller_register"),
    path('register/customer/',views.customer_register, name="customer_register"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('my-orders/', views.customer_orders, name='customer_orders'),
    path('my-orders/', views.my_orders, name='my_orders'),


]
