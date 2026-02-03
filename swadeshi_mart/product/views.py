from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from product.forms import ProductForm
from .models import Product

# Create your views here.

def prodeuc_detail(request,pk):
    product = get_object_or_404(Product,pk=pk)
    return render(request,'product/product_detail.html',{'product':product})