from django.contrib import admin
from django.urls import path, include
from .views import home  
from Sendex_App.views import home_view  # Import the view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Add this line for the root URL
    path('register/', include('Sendex_App.urls')),
    path('login/', include('Sendex_App.urls')),
    path('dashboard/', include('Sendex_App.urls')),
    path('send-item/', include('Sendex_App.urls')),
    path('receive-item/', include('Sendex_App.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Include auth URLs

]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', home, name='home'),
#     # path('', include('accounts.urls')),
#     path('place_order/', include('orders.urls', namespace='orders')),
#     # path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
#     path('register/', include('accounts.urls')), 
#     path('place_orders/', include('orders.urls')),
# ]
