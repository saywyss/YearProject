from django.contrib import admin
from django.urls import path
from . import views

from main.views import ProfileView, OrderView, InfoView, CatalogView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('info/', InfoView.as_view(), name='info'),
    path('list_order/', OrderView.as_view(), name='order'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]

