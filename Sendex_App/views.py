from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# def home(request):
#     return render(request, 'home.html')
def home_view(request):
    return render(request, 'home.html')
def register_view(request):
    return render(request, 'registration.html')

def login_view(request):
    return render(request, 'login.html')

def dashboard_view(request):
    return render(request, 'dashboard.html', {'user': request.user})

def send_item_view(request):
    return render(request, 'send_item.html')

def receive_item_view(request):
    return render(request, 'receive_item.html')

# def user_dashboard(request):
#     return render(request, 'accounts/user_dashboard.html')

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})

