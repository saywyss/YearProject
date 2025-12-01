from django.contrib import admin
from django.urls import path

from main.views import ProfileView, OrderView, InfoView, CatalogView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('home.html', HomeView.as_view(), name='index'),
    path('catalog.html', CatalogView.as_view(), name='catalog'),
    path('info.html', InfoView.as_view(), name='info'),
    path('list_orders.html', OrderView.as_view(), name='order'),
    path('profile.html', ProfileView.as_view(), name='profile'),
]

