from django.db import models

from Facturas.models import Factura

class Pago(models.Model):
    monto = models.IntegerField()
    tipo = models.CharField(max_length=100)
    fecha = models.DateField()
    id = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    
        
    def __str__(self):
        return f'Pago{self.id}'