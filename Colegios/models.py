from django.db import models

# Create your models here.
class Colegio(models.Model):
    id = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    cursos = models.IntegerField()
    
class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    anio = models.CharField(max_length=100)
    fecha = models.DateField()
    nombre = models.CharField(max_length=100)
    colegio = models.ForeignKey(Colegio,on_delete=models.CASCADE)