from django.contrib import messages
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

# def place_order(request):
#     return render(request, 'orders/place_order.html')

# def order_history(request):
#     return render(request, 'orders/order_history.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'register/login.html')

# class LandingView(TemplateView):

# 	template_name = 'templates/index.html'


# class DashboardView(TemplateView):

# 	template_name = 'templates/dashboard.html'