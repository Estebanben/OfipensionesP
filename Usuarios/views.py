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
        return render(request, 'Usuarios/templates/estudiantes_list.html', context)
    else:
        return HttpResponse('No tienes permisos para ver esta pagina')
    
        