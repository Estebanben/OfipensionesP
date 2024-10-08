from ..models import Pago

def getPagos():
    pagos = Pago.objects.all()
    return pagos
