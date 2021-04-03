from django.shortcuts import render, redirect
import sqlite3
from supermarket.models import product

class AltaProductos():

    def __init__(self, name, cantidad):
        self.name = name
        self.cantidad = cantidad

def control_product(request):
    """manage different actions over product"""

    if request.method == 'GET':
        return render(request, 'control.html')

    elif request.method == 'POST':
        # import pdb; pdb.set_trace()
        name = request.POST['nombre']
        qty = request.POST['cantidad']
        action = request.POST['action']

        if action == 'Ver_Lista':
            cesta = product.objects.all()
            return render(request, 'list.html', {'cesta': cesta})

        elif action == 'Guardar':
            producto = AltaProductos(name,qty)
            product.objects.create(name = producto.name, cantidad = producto.cantidad)
            message = 'Saved'
    
        elif action == 'Modificar':
            producto = product.objects.get(name=name)
            producto.cantidad = qty
            producto.save()
            message = 'Modified'
        
        elif action == 'Borrar':
            producto = product.objects.get(name=name)
            producto.delete()
            message = 'Deleted'

        cesta = product.objects.all()
        return render(request, 'list.html', {
            'producto': producto, 
            'mensaje': 'Product {}'.format(message), 
            'cesta': cesta
            })

def product_list(request):
    """to show the list with all products"""
    if request.method == 'GET':
        cesta = product.objects.all()
        return render(request, 'list.html', {'cesta': cesta})
    elif request.method == 'POST':
        return render(request, 'control.html')

