from django.shortcuts import render
from django.http import HttpResponse
from Facturas.models import Producto

PALABRAS_RESERVADAS = ['DELETE', 'DROP', 'INSERT', 'UPDATE', '--', ';', 'SELECT']

def prueba_inyeccion_sql(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')

        for palabra in PALABRAS_RESERVADAS:
            if any(palabra in campo for campo in [nombre, precio, descripcion]):
                return HttpResponse('Error: Entrada no permitida debido a palabras reservadas', status=400)

        try:
            Producto.objects.create(nombre=nombre, valor=precio, dscripcion=descripcion)
            return HttpResponse('El producto creado exitosamente')
        except Exception as e:
            return HttpResponse(f'Error al crear el producto: {str(e)}')

    return render(request, 'formulario.html')
