from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

# app_name = 'Sendex_App'
# urlpatterns = [
#     path('register/', views.register, name='register'),
#     path('login/', views.custom_login, name='login'),
#     path('profile/', views.profile, name='profile'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
#     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
#     path('dashboard/', views.user_dashboard, name='user_dashboard'),
#     path('', views.home, name='home'),
#     # path('register/', include('accounts.urls')), 
#     path('place_orders/', include('orders.urls')),
# ]

urlpatterns = [
    path('home/', views.home_view, name='home'),
    # path('register/', views.register_view, name='register'),
    # path('login/', views.login_view, name='login'),
    # path('dashboard/', views.dashboard_view, name='dashboard'),
    # path('send-item/', views.send_item_view, name='send_item'),
    # path('receive-item/', views.receive_item_view, name='receive_item'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
