from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('login/', views.login, name='login_page'),
    path('refresh/', views.refresh_token, name='refresh_token'),
    path('orders/view/<str:order_id>', views.view_order, name='view order')
]