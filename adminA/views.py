from django.shortcuts import render
from adminA import*

# Create your views here.
def indexVol(request):
    return render(request, 'indexVol.html')

def indexHotel(request):
    return render(request, 'indexHotel.html')

def indexBus(request):
    return render(request, 'indexBus.html')


