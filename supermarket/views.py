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

        if request.POST['action'] == 'Guardar':
            producto = AltaProductos(request.POST['nombre'],request.POST['cantidad'])

            # Add products
            product.objects.create(name = producto.name, cantidad = producto.cantidad)

            return render(request, 'saved.html', {'producto': producto, 'mensaje': 'Articulo guardado'})
    
        elif request.POST['action'] == 'Modificar':
            producto = product.objects.get(name=request.POST['nombre'])
            producto.cantidad = request.POST['cantidad']
            producto.save()
            return render(request, 'saved.html', {'producto': producto, 'mensaje': 'Articulo modificado'})
        
        elif request.POST['action'] == 'Borrar':
            producto = product.objects.get(name=request.POST['nombre'])
            producto.delete()
            return render(request, 'saved.html', {'producto': producto, 'mensaje': 'Articulo eliminado'})

        elif request.POST['action'] == 'Ver_Lista':
            cesta = product.objects.all()
            return render(request, 'panel.html', {'cesta': cesta})


def panel(request):

    if request.method == 'POST':
        return render(request, 'saved.html')

    else:
        cesta = product.objects.all()
        return render(request, 'panel.html', {'cesta': cesta})

