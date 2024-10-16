from django.db import models

from Usuarios.models import Estudiante
from Facturas.models import CronogramaDePago
from Colegios.models import Curso,Colegio

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    precio = models.IntegerField()
    fechaIni = models.CharField(max_length=100)
    fechaVen = models.CharField(max_length=100)
    abonado = models.IntegerField()
    intereses = models.IntegerField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    cronograma = models.ForeignKey(CronogramaDePago, on_delete=models.CASCADE)

    def __str__(self):
        return f'Factura ID: {self.id} | Estudiante: {self.estudiante.nombre} | Fecha de Inicio: {self.fechaIni} | Valor: {self.precio} | Fecha de Vencimiento: {self.fechaVen}'




class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.IntegerField()
    dscripcion = models.CharField(max_length=1000)
    
    def __init__(self, nombre, valor, descripcion):
        self.nombre = nombre
        self.valor = valor
        self.descripcion = descripcion
    
    def __str__(self):
        return self.nombre

class CronogramaDePago(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso)
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCASDE)


class DetalleCronograma(models.Model):
    id = models.AutoField(primary_key=True)
    valor = models.IntegerField(max_length=100)
    fechaCausacion = models.DateField()
    fechaLimite = models.DateField()
    cronograma = models.ForeignKey(CronogramaDePago, on_delete=models.CASCADE)