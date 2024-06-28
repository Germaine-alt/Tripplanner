from django.urls import path
from . import views

urlpatterns = [
    path("indexVol", views.indexVol, name="indexVol"),
    path("indexHotel", views.indexHotel, name="indexHotel"),
    path("indexBus", views.indexBus, name="indexBus"),


]

