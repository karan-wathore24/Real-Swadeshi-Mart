from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout

from .forms import SellerRegisterForm, CustomerRegisterForm

from orders.models import Order


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

            # ✅ ADMIN = direct admin panel
            if user.is_superuser:
                return redirect('/admin/')

            # ✅ respect ?next= for normal users
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)

            # ✅ default = shop/home
            return redirect('/')

        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


from django.contrib.auth.decorators import login_required

@login_required
def customer_dashboard(request):
    return redirect('/')



def logout_view(request):
    logout(request)     
    return redirect('login')


@login_required
def customer_dashboard(request):
    user = request.user

    # sirf customer allow
    if not user.is_customer:
        return redirect('/')

    orders = Order.objects.filter(user=user).order_by('-created_at')

    return render(request, 'accounts/customer_dashboard.html', {
        'user': user,
        'orders': orders
    })


@login_required
def customer_orders(request):
    if not request.user.is_customer:
        return redirect('/')

    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'accounts/my_orders.html', {
        'orders': orders
    })
@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'accounts/my_orders.html', {'orders': orders})