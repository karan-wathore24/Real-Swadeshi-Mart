from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from product.forms import ProductForm




@login_required
def seller_dashboard(request):
    if not request.user.is_seller:
        return redirect('login')
    return render(request,"seller/dashboard.html")



@login_required(login_url='login')
def add_product(request):
    if not request.user.is_seller:
        return redirect('login')
    
    if request.method=='POST':
        form= ProductForm(request.POST,request.FILES)
        if form.is_valid():
            product= form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('seller_dashboard')
    else:
        form= ProductForm()

    return render(request, 'seller/add_product.html',{'form':form})
