from django.shortcuts import render, redirect
import sqlite3
from supermarket.models import product

class AltaProductos():
    name = ""
    cantidad = ""

    def __init__(self, name, cantidad):
        self.name = name
        self.cantidad = cantidad

def save_product(request):


    if request.method == 'POST':
        # import pdb; pdb.set_trace()

        name = request.POST['nombre']
        qty = request.POST['cantidad']
        action = request.POST['action']

        if action == 'Guardar':
            producto = AltaProductos(name,qty)

            # Add products
            product.objects.create(name = producto.name, cantidad = producto.cantidad)

            return render(request, 'saved.html', {'producto': producto, 'mensaje': 'Articulo guardado'})
    
        elif action == 'Modificar':
            producto = product.objects.get(name=name)
            producto.cantidad = qty
            producto.save()
            return render(request, 'saved.html', {'producto': producto, 'mensaje': 'Articulo modificado'})
        
        elif action == 'Borrar':
            producto = product.objects.get(name=name)
            producto.delete()
            return render(request, 'saved.html', {'producto': producto, 'mensaje': 'Articulo eliminado'})

        elif action == 'Ver_Lista':
            cesta = product.objects.all()
            return render(request, 'panel.html', {'cesta': cesta})


def panel(request):

    if request.method == 'POST':
        return render(request, 'saved.html')

    else:
        cesta = product.objects.all()
        return render(request, 'panel.html', {'cesta': cesta})

