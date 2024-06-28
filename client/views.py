from django.shortcuts import render
from client import*

# Create your views here.
def index(request):
    return render(request, 'index.html')
