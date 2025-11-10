from django.contrib import admin
from django.urls import path
from main.views import HomeView
from main.views import CatalogView
from main.views import InfoView
from main.views import OrderView
from main.views import ProfileView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('info/', InfoView.as_view(), name='info'),
    path('order/<int:order_id>', OrderView.as_view(), name='order'),
    path('profile/<int:user_id>', ProfileView.as_view(), name='profile'),
    
]

