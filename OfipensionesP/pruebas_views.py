from django.http import JsonResponse
from Facturas.models import Factura

def prueba_inyeccion_sql(request):
    # Extrae parámetros de la URL
    nombre = request.GET.get('nombre', 'Factura de prueba')
    monto = request.GET.get('monto', '100')
    
    # Crea un objeto usando el ORM de Django
    factura = Factura(nombre=nombre, monto=monto)
    factura.save()  # ORM protege contra inyección SQL en este método

    # Responde con un JSON que confirma la creación
    return JsonResponse({'status': 'Factura creada', 'nombre': factura.nombre, 'monto': factura.monto})
