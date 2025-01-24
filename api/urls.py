from django.urls import path
from . import views

urlpatterns = [
    path('orders/create', views.create_new_order, name='api_create_new_order'),
    path('orders/all', views.get_all_orders, name='api_get_all_orders'),
    path('orders/update/<str:id>', views.update_order, name='api_update_order'),
    path('orders/delete/<str:id>', views.delete_order, name='api_delete_order'),
    path('orders/status/<str:id>', views.get_order_status, name='api_get_order_status')
]