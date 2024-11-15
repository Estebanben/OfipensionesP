from django.shortcuts import render
from django.http import HttpResponse
from Facturas.models import Producto  

def prueba_inyeccion_sql(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')
        try:
            Producto.objects.create(nombre=nombre, valor=precio, dscripcion=descripcion)
            return HttpResponse('Producto creado exitosamente.')
        except Exception as e:
            return HttpResponse(f'Error al crear el producto: {str(e)}')
    return render(request, 'formulario.html')