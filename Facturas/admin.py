from django.contrib import admin
from .models import CronogramaDePago, Factura
from .models import Producto
# Register your models here.
admin.site.register(Factura)
admin.site.register(Producto)
admin.site.register(CronogramaDePago)