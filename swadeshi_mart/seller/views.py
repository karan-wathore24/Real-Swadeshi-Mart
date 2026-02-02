from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def seller_dashboard(request):
    if not request.user.is_seller:
        return redirect('login')
    return render(request,"seller/dashboard.html")
