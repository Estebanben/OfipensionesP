from django.shortcuts import render
from django.shortcuts import redirect
from .models import Estudiante, Padre

def hijos_del_padre(request):
    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        try:
            # Obtiene el padre a partir del usuario autenticado
            padre = Padre.objects.get(correo=request.user.email)
            # Obtiene los hijos asociados a este padre
            hijos = Estudiante.objects.filter(padre=padre)
        except Padre.DoesNotExist:
            # Si el padre no existe, retorna una lista vacía
            hijos = []

        # Renderiza los datos de los hijos en el template
        return render(request, 'hijos_del_padre.html', {'hijos': hijos})
    else:
        # Redirige a la página de inicio de sesión si no está autenticado
        return render(request, 'hijos_del_padre.html', {'hijos': hijos})