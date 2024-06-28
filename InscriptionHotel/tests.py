from django.urls import path
from . import views


urlpatterns = [
    path("login", views.login, name="login"),
    path("loginClient", views.loginClient, name="loginClient"),
    path("register", views.register, name="register"),
    path('registerClient', views.registerClient, name='registerClient'),
    path("logout", views.logout, name="logout"),



]

