from ..models import Estudiante

def getEstudiantes(request):
    user = request.user
    return Estudiante.objects.filter(padre=user)

def createEstudiante(form):
    estudiante = estudiante.save()
    estudiante.save()
    estudiante ()

def createEstudianteObject(nombre, fecha_nacimiento, tipo_d, documento, genero, correo, contraseña, saldo, padre):
    estudiante = Estudiante()
    estudiante.nombre = nombre
    estudiante.fecha_nacimiento = fecha_nacimiento
    estudiante.tipo_d = tipo_d
    estudiante.documento = documento
    estudiante.genero = genero
    estudiante.correo = correo
    estudiante.contraseña = contraseña
    estudiante.saldo = saldo
    estudiante.padre = padre
    estudiante.save()
    return()

def getEstudiante(id):
    estudiante = Estudiante.objects.get(id=id)
    return estudiante
    
