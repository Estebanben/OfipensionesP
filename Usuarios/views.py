from django.shortcuts import render
from .logic.logicEstudiantes import getEstudiantes
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Autenticacion.auth0backend import getRole

@login_required
def estudiantes_list(request):
    role = getRole(request)
    if role == 'Padre':
        estudiantes = getEstudiantes()
        context = {'estudiantes_list': estudiantes}
        return render(request, 'Estudiante/estudiantes.html', context)
    else:
        return HttpResponse('No tienes permisos para ver esta pagina')
# Create your views here.
# @login_required
# def estudiantes_list(request):
#     role = getRole(request)
#     if role == 'Padre':
#         estudiantes = getEstudiantes(request)
#         context = {'estudiantes_list': estudiantes}
#         return render(request, 'Estudiante/estudiantes.html', context)
#     else:
#         return HttpResponse('No tienes permisos para ver esta pagina')
        