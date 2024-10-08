from django.shortcuts import render
from Pagos.logic import logicPagos
from django.core import serializers
from django.http import HttpResponse
# Create your views here.
def pagosView(request):
    if request.method == 'GET':
        pagos = logicPagos.getPagos()
        pagosDto = serializers.serialize('json',pagos)
        return HttpResponse(pagosDto,'application/json')