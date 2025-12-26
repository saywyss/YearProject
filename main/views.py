from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

from main.models import Product
from main.models import Order

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
    def post(self, request):
        pass

class CatalogView(View):
    def get(self, request):
        all_products = Product.objects.all()
        
        return render(request, 'catalog.html', {
            "all_products": all_products
        })
    
    def post(self, request):
        pass

class InfoView(View):
    def get(self, request):
        return render(request, 'info.html')
    def post(self, request):
        pass

class ListOrderView(LoginRequiredMixin, View):
    def get(self, request):
        all_orders = Order.objects.filter(user=request.user)
        return render(request, 'view.html', {"all_orders": all_orders})
    def post(self, request):
        pass

class DetailOrderView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'view.html')
    def post(self, request):
        pass

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'profile.html')
    def post(self, request):
        pass

class OrderView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'order.html')
    def post(self, request):
        pass


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product.id)] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': cart.get(str(product.id), {}).get('quantity', 0) + 1
        }


    request.session['cart'] = cart
    return redirect('catalog')


def cart_view(request):
    cart = request.session.get('cart', {})

    total_price = sum(
        float(item['price']) * item['quantity']
        for item in cart.values()
    )

    context = {
        'cart': cart,
        'total_price': total_price,
    }

    return render(request, 'cart.html', context)
