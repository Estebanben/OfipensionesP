from django.shortcuts import render
from .logic.logicEstudiantes import getEstudiantes
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Autenticacion.auth0backend import getRole


# Create your views here.
@login_required
def estudiantes_list(request):
    role = getRole(request)
    if role == 'Padre':
        estudiantes = getEstudiantes(request)
        context = {'estudiantes_list': estudiantes}
        return render(request, 'Estudiante/estudiantes.html', context)
    else:
        return HttpResponse('No tienes permisos para ver esta pagina')
    
# def hijos_del_padre(request):
#     # Verifica si el usuario está autenticado
#     if request.user.is_authenticated:
#         try:
#             # Obtiene el padre a partir del usuario autenticado
#             padre = Padre.objects.get(correo=request.user.email)
#             # Obtiene los hijos asociados a este padre
#             hijos = Estudiante.objects.filter(padre=padre)
#         except Padre.DoesNotExist:
#             # Si el padre no existe, retorna una lista vacía
#             hijos = []

#         # Renderiza los datos de los hijos en el template
#         return render(request, 'hijos_del_padre.html', {'hijos': hijos})
#     else:
#         # Redirige a la página de inicio de sesión si no está autenticado
#         return render(request, 'hijos_del_padre.html', {'hijos': hijos})
    
        