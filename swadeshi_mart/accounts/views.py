from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SellerRegisterForm, CustomerRegisterForm

# Create your views here.
def seller_register(request):
    if request.method == 'POST':
        form = SellerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SellerRegisterForm()

    return render(request, 'accounts/seller_register.html', {'form': form})


def customer_register(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomerRegisterForm()

    return render(request, 'accounts/customer_register.html', {'form': form})
            
