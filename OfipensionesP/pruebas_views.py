from django.http import JsonResponse
from Facturas.models import Producto  # Ajusta la importación al módulo correcto

def prueba_inyeccion_sql(request):
    # Extrae los parámetros de la URL
    nombre = request.GET.get('nombre', 'Producto de prueba')
    valor = request.GET.get('valor', '100')
    descripcion = request.GET.get('descripcion', 'Descripción de prueba')

    # Crea un objeto usando el modelo Producto
    producto = Producto(nombre=nombre, valor=valor, dscripcion=descripcion)
    producto.save()  # Guarda el producto en la base de datos

    # Responde con un JSON que confirma la creación
    return JsonResponse({
        'status': 'Producto creado',
        'nombre': producto.nombre,
        'valor': producto.valor,
        'descripcion': producto.descripcion
    })
