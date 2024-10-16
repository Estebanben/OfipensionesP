from io import StringIO
from django.db import models
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from Usuarios.models import Estudiante
from Colegios.models import Curso,Colegio
import pandas as pd


class CronogramaDePago(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso)
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)
    
    @staticmethod
    def getFacturasRango(startDate,endDate,colegio_id):
        return Factura.objects.filter(fechaIni__range= (startDate,endDate),cronograma__colegio__id=colegio_id)
    def saveFacturasToCSV(startDate, endDate, colegio_id, filename='facturas.csv'):
        facturas = CronogramaDePago.getFacturasRango(startDate, endDate, colegio_id)

        # Crear un DataFrame de pandas
        data = {
            'ID': [],
            'Tipo': [],
            'Precio': [],
            'Fecha Inicio': [],
            'Fecha Vencimiento': [],
            'Abonado': [],
            'Intereses': [],
            'Estudiante': [],
        }

        for factura in facturas:
            data['ID'].append(factura.id)
            data['Tipo'].append(factura.tipo)
            data['Precio'].append(factura.precio)
            data['Fecha Inicio'].append(factura.fechaIni)
            data['Fecha Vencimiento'].append(factura.fechaVen)
            data['Abonado'].append(factura.abonado)
            data['Intereses'].append(factura.intereses)
            data['Estudiante'].append(factura.estudiante.nombre)

        df = pd.DataFrame(data)

        # Guardar el DataFrame en un archivo CSV
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)

        # Guardar el archivo en el sistema de archivos
        file_path = f'media/{filename}'
        default_storage.save(file_path, ContentFile(csv_buffer.getvalue()))

        return file_path


class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    precio = models.IntegerField()
    fechaIni = models.DateField()
    fechaVen = models.DateField()
    abonado = models.IntegerField()
    intereses = models.IntegerField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    cronograma = models.ForeignKey(CronogramaDePago, on_delete=models.CASCADE,null = True)

#    def __str__(self):
#        return f'Factura ID: {self.id} | Estudiante: {self.estudiante.nombre} | Fecha de Inicio: {self.fechaIni} | Valor: {self.precio} | Fecha de Vencimiento: {self.fechaVen}'




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