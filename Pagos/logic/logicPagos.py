from ..models import Pago

def getPagos():
    pagos = Pago.objects.all()
    return pagos

def createPago(form):
    pago = form.save()
    pago.save()
    return ()

def createPagoObject(monto,tipo,fecha,id,factura):
    pago = Pago()
    pago.monto = monto
    pago.tipo = tipo
    pago.fecha = fecha
    pago.id = id
    pago.factura = factura
    pago.save()
    return()
    
