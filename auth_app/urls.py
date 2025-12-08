from django.contrib import admin
from django.urls import path
from auth_app.views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('register.html', RegisterView.as_view(), name="register"),
    path('login.html', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]