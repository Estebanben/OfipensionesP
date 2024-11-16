from ..models import Estudiante, Padre

def getEstudiantes(request):
    # Obtener la instancia del padre asociada al usuario
    try:
        padre = Padre.objects.get(correo=request.user.email)  # Ajusta el campo `user` según tu modelo Padre
    except Padre.DoesNotExist:
        return []  # Devuelve una lista vacía si no se encuentra al padre

    # Filtrar estudiantes relacionados con este padre
    return Estudiante.objects.filter(padre=padre)

# def getEstudiantes():
#     queryset = Estudiante.objects.all()
#     return queryset

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
    
