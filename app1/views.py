from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout

@login_required
@require_POST
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.delete()
    return redirect('order_history')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.session.setdefault('cart', []).append(product_id)
    request.session.modified = True
    return redirect('product_list')

def checkout(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    for product in products:
        Order.objects.create(user=request.user, product=product)
    request.session['cart'] = []
    return redirect('order_history')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def order_history(request):
    if request.user.is_authenticated:  # Ensure the user is authenticated
        orders = Order.objects.filter(user=request.user)
        return render(request, 'orders.html', {'orders': orders})
    else:
        return redirect('user_login')  # Redirect to login if the user is not authenticated

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')  # Redirect to user dashboard
        else:
            return render(request, 'user_login.html', {'error': 'Invalid credentials'})
    return render(request, 'user_login.html')

def vendor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if hasattr(user, 'vendor'):  # Check if user is a vendor
                login(request, user)
                return redirect('vendor_dashboard')  # Redirect to vendor dashboard
            else:
                return render(request, 'vendor_login.html', {'error': 'Not a vendor account'})
        else:
            return render(request, 'vendor_login.html', {'error': 'Invalid credentials'})
    return render(request, 'vendor_login.html')

def logout_view(request):
    logout(request)
    return redirect('home') 
def home(request):
    return render(request,'home.html')
