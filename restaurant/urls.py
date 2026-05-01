from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # important
    path('menu/', views.menu_list, name='menu_list'),
    path('tables/', views.table_list, name='table_list'),
    path('orders/', views.order_list, name='order_list'),
    path('add-order/', views.add_order, name='add_order'),
]