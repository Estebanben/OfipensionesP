# Facturas/urls.py
from django.urls import path
from .views import generar_facturas_csv

urlpatterns = [
    path('generar-facturas-csv/', generar_facturas_csv, name='generar_facturas_csv'),
]
