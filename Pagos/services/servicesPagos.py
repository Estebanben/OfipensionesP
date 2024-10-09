from OfipensionesP.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def send_email():
    subject = "test"
    message = "pago creado"
    recipient = "e.benavidesv@uniandes.edu.co"
    send_mail(subject,message,EMAIL_HOST_USER,[recipient])