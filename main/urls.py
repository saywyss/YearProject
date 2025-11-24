from django.contrib import admin
from django.urls import path
from main.views import HomeView
from main.views import CatalogView
from main.views import InfoView
from main.views import OrderView
from main.views import ProfileView

urlpatterns = [
    path('home.html', HomeView.as_view(), name='home'),
    path('catalog.html', CatalogView.as_view(), name='catalog'),
    path('info.html', InfoView.as_view(), name='info'),
    path('list_orders.html', OrderView.as_view(), name='order'),
    path('profile.html', ProfileView.as_view(), name='profile'),
    path('login.html', ProfileView.as_view(), name='login'),
    path('register.html', ProfileView.as_view(), name='register'),
    
]

