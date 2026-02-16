from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render,get_object_or_404
# from cart.models import Cart
from .models import Order

@login_required
def place_order(request):
    user = request.user

    cart_items = Order.objects.filter(user=user)
    if not cart_items.exists():
        return redirect('/cart/')

    total = sum(item.product.price * item.quantity for item in cart_items)

    order = Order.objects.create(
        user=user,
        total_price=total,
        status='Placed'
    )

    cart_items.delete()  # cart clear after order

    return redirect('/accounts/dashboard/')

@login_required
def order_detail(request, id):
    order = get_object_or_404(Order, id=id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})