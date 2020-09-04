"""proyecto URL Configuration
"""
from django.contrib import admin
from django.urls import path
from supermarket import views

urlpatterns = [
    path('save/', views.save_product, name='save'),
    path('panel/', views.panel, name='lista_compra'),
]
