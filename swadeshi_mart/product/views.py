from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from product.forms import ProductForm
from .models import Product

def shop(request):
    products = Product.objects.all()
    return render(request, 'product/shop.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product/product_detail.html', {'product': product})
