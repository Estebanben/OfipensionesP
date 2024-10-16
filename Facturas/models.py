from django.db import models

from Usuarios.models import Estudiante
from Colegios.models import Curso,Colegio


class CronogramaDePago(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso)
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)
    
    @staticmethod
    def getFacturasRango(startDate,endDate,colegio_id):
        return Factura.objects.filter(fechaIni__range= (startDate,endDate),cronograma__colegio__id=colegio_id)


class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    precio = models.IntegerField()
    fechaIni = models.DateField()
    fechaVen = models.DateField()
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

    
    


class DetalleCronograma(models.Model):
    id = models.AutoField(primary_key=True)
    valor = models.IntegerField()
    fechaCausacion = models.DateField()
    fechaLimite = models.DateField()
    cronograma = models.ForeignKey(CronogramaDePago, on_delete=models.CASCADE)