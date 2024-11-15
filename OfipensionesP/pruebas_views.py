from django.http import JsonResponse
from Pagos.models import Pago  # Asegúrate de que esta sea la ruta correcta de tu modelo

def prueba_inyeccion_sql(request):
    # Extrae los parámetros de la URL
    nombre = request.GET.get('nombre', 'Pago de prueba')
    monto = request.GET.get('monto', '100')
    descripcion = request.GET.get('descripcion', 'Descripción de prueba')

    # Crea un objeto usando el modelo Pago
    pago = Pago(nombre=nombre, monto=monto, descripcion=descripcion)
    pago.save()  # Guarda el pago en la base de datos

    # Responde con un JSON que confirma la creación
    return JsonResponse({
        'status': 'Pago creado',
        'nombre': pago.nombre,
        'monto': pago.monto,
        'descripcion': pago.descripcion
    })
