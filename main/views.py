from django.shortcuts import render
from django.views.generic import View

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

class ListOrderView(View):
    def get(self, request):
        all_orders = Order.objects.filter(user=request.user)
        return render(request, 'view.html', {"all_orders": all_orders})
    def post(self, request):
        pass

class DetailOrderView(View):
    def get(self, request):
        return render(request, 'view.html')
    def post(self, request):
        pass

class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')
    def post(self, request):
        pass

class OrderView(View):
    def get(self, request):
        return render(request, 'order.html')
    def post(self, request):
        pass