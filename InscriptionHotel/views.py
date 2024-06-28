# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .forms import RegisterForm, RegisterClientForm
from django.contrib import messages



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('indexBus')  # Rediriger vers le tableau de bord
            else:
                error = 'Email ou mot de passe incorrect.'
        except User.DoesNotExist:
            error = 'Email ou mot de passe incorrect.'
        return render(request, 'connexion/loginH.html', {'error': error})
    return render(request, 'connexion/loginH.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Rediriger vers la page de connexion après l'inscription
        else:
            return render(request, 'connexion/registerH.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'connexion/registerH.html', {'form': form})




def registerClient(request):
    if request.method == 'POST':
        form = RegisterClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginClient')  # Rediriger vers la page de connexion après l'inscription
        else:
            return render(request, 'connexion/registerH.html', {'form': form})
    else:
        form = RegisterClientForm()
    return render(request, 'connexion/registerH.html', {'form': form})




def loginClient(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')  # Rediriger vers le tableau de bord
            else:
                error = 'Email ou mot de passe incorrect.'
        except User.DoesNotExist:
            error = 'Email ou mot de passe incorrect.'
        return render(request, 'connexion/loginH.html', {'error': error})
    return render(request, 'connexion/loginH.html')







def hotelR(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Rediriger vers la page de connexion après l'inscription
        else:
            return render(request, 'connexion/hotelR.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'connexion/hotelR.html', {'form': form})

def busR(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Rediriger vers la page de connexion après l'inscription
        else:
            return render(request, 'connexion/busR.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'connexion/busR.html', {'form': form})

def volR(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Rediriger vers la page de connexion après l'inscription
        else:
            return render(request, 'connexion/volR.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'connexion/volR.html', {'form': form})



def clientR(request):
    if request.method == 'POST':
        form = RegisterClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Rediriger vers la page de connexion après l'inscription
        else:
            return render(request, 'connexion/clientR.html', {'form': form})
    else:
        form = RegisterClientForm()
    return render(request, 'connexion/clientR.html', {'form': form})





def logout(request):
    auth_logout(request)
    return redirect('connexion/login')


def bus(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('indexBus')  # Rediriger vers le tableau de bord
            else:
                error = 'Email ou mot de passe incorrect.'
        except User.DoesNotExist:
            error = 'Email ou mot de passe incorrect.'
        return render(request, 'connexion/bus.html', {'error': error})
    return render(request, 'connexion/bus.html')

def vol(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('indexVol')  # Rediriger vers le tableau de bord
            else:
                error = 'Email ou mot de passe incorrect.'
        except User.DoesNotExist:
            error = 'Email ou mot de passe incorrect.'
        return render(request, 'connexion/vol.html', {'error': error})
    return render(request, 'connexion/vol.html')

def hotel(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('indexHotel')  # Rediriger vers le tableau de bord
            else:
                error = 'Email ou mot des passe incorrect.'
        except User.DoesNotExist:
            error = 'Email ou mot de passe incorrect.'
        return render(request, 'connexion/hotel.html', {'error': error})
    return render(request, 'connexion/hotel.html')



def client(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')  # Rediriger vers le tableau de bord
            else:
                error = 'Email ou mot des passe incorrect.'
        except User.DoesNotExist:
            error = 'Email ou mot de passe incorrect.'
        return render(request, 'connexion/client.html', {'error': error})
    return render(request, 'connexion/client.html')


