"""proyecto URL Configuration
"""
from django.contrib import admin
from django.urls import path
from supermarket import views

urlpatterns = [
    path('panel_control/', views.control_product, name='controla_producto'),
    path('list/', views.product_list, name='lista_compra'),
]
