from django.urls import path
from . import views


urlpatterns = [
    path("login", views.login, name="login"),
    path("loginClient", views.loginClient, name="loginClient"),
    path("register", views.register, name="register"),
    path('registerClient/', views.registerClient, name='registerClient'),
    path("logout", views.logout, name="logout"),
    path("bus", views.bus, name="bus"),
    path("vol", views.vol, name="vol"),
    path("hotel", views.hotel, name="hotel"),
    path("busR", views.busR, name="busR"),
    path("volR", views.volR, name="volR"),
    path("hotelR", views.hotelR, name="hotelR"),
    path("client", views.client, name="client"),
    path("clientR", views.clientR, name="clientR"),


   




]

