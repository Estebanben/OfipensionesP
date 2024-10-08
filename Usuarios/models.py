from django.db import models

class Estudiante(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    TIPO_D_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        # Agrega más opciones si es necesario
    ]

    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    tipo_d = models.CharField(max_length=2, choices=TIPO_D_CHOICES)
    documento = models.CharField(max_length=20, unique=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    saldo = models.IntegerField()

    def __str__(self):
        return self.nombre

class Padre(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    TIPO_D_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
    ]

    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    tipo_d = models.CharField(max_length=2, choices=TIPO_D_CHOICES)
    documento = models.CharField(max_length=20, unique=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre