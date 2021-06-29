from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from account.forms import UserEditForm

from django.urls import reverse
from django.shortcuts import redirect



def order_create(request):
    cart = Cart(request)
    # if request.method == 'POST':
    form = OrderCreateForm(request.POST)
    user_form = UserEditForm(instance=request.user, data=request.POST)
    if form.is_valid() and user_form.is_valid():
        order = form.save()
        user_form.save()
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'],  price=item['price'], quantity=item['quantity'])
        
        # clear the cart
        cart.clear()
        return render(request, 'orders/order/created.html', {'order': order, 'cart':cart})
    else:
        form = OrderCreateForm()
    
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form, 'user_form': user_form})