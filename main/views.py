from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
    def post(self, request):
        pass

class CatalogView(View):
    def get(self, request):
        return render(request, 'catalog.html')
    def post(self, request):
        pass

class InfoView(View):
    def get(self, request):
        return render(request, 'info.html')
    def post(self, request):
        pass

class OrderView(View):
    def get(self, request):
        return render(request, 'view.html')
    def post(self, request):
        pass

class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')
    def post(self, request):
        pass