from django.http import JsonResponse
from Facturas.models import Producto 

def prueba_inyeccion_sql(request):
    nombre = request.GET.get('nombre', 'Producto de prueba')
    valor = request.GET.get('valor', '100')
    descripcion = request.GET.get('descripcion', 'Descripción de prueba')

    producto = Producto(nombre=nombre, valor=valor, dscripcion=descripcion)
    producto.save() 

    return JsonResponse({
        'status': 'Producto creado',
        'nombre': producto.nombre,
        'valor': producto.valor,
        'descripcion': producto.dscripcion
    })
