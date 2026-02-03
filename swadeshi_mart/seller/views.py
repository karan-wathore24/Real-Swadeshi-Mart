from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from product.forms import ProductForm
from product.models import Product



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

@login_required(login_url='login')
def seller_products(request):
    if not request.user.is_seller:
        return redirect('login')

    products = Product.objects.filter(seller=request.user)
    return render(request, 'seller/product_list.html', {
        'products': products
    })

@login_required(login_url='login')
def edit_product(request, pk):
    if not request.user.is_seller:
        return redirect('login')

    product = Product.objects.get(pk=pk, seller=request.user)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('seller_products')
    else:
        form = ProductForm(instance=product)

    return render(request, 'seller/edit_product.html', {'form': form})

@login_required(login_url='login')
def delete_product(request, pk):
    if not request.user.is_seller:
        return redirect('login')

    product = Product.objects.get(pk=pk, seller=request.user)

    if request.method == 'POST':
        product.delete()
        return redirect('seller_products')

    return render(request, 'seller/delete_product.html', {'product': product})
