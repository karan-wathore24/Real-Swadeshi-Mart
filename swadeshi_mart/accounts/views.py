from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout

from .forms import SellerRegisterForm, CustomerRegisterForm

# Create your views here.


def home(request):
    return render(request,"home.html")


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

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('/admin/')
            elif user.is_seller:
                return redirect('seller_dashboard')
            elif user.is_customer:
                return redirect('customer_home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')
            
def customer_home(request):
    return HttpResponse("Customer Home Page")

def logout_view(request):
    logout(request)     
    return redirect('login')