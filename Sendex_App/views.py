# Sendex_App/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from Sendex_App.models import Shipment
from .forms import ShipmentForm



def home_view(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    user_shipments = Shipment.objects.filter(user=request.user)
    return render(request, 'dashboard/dashboard.html', {'user_shipments': user_shipments})

@login_required
def create_shipment(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            shipment = form.save(commit=False)
            shipment.user = request.user
            shipment.save()
            return redirect('dashboard')
    else:
        form = ShipmentForm()
    
    return render(request, 'dashboard/create_shipment.html', {'form': form})

def track_shipment(request):
    # Your view logic here
    return render(request, 'track_shipment.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the user's dashboard
    return render(request, 'registration/login.html')
