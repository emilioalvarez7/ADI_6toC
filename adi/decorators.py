#En este archivo se crean todas las restricciones de acceso
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import AnonymousUser, User, Group
"""
#Funcion para entrar al perfil del alumno
def check_Alumno_o_Tutor(user):
    if Group.objects.get(name='Alumno_o_Tutor') in user.groups.all():
        return True
    return False
"""
#Funcion para entrar a direccion
def check_Director(user):
    if Group.objects.get(name='Director') in user.groups.all():
        return True
    return False
"""
#Funcion para entrar a la guardia
def check_Guardia(user):
    if Group.objects.get(name='Guardia') in user.groups.all():
        return True
    return False
"""
#Funcion para entrar a la preceptoria
def check_Preceptor(user):
    if Group.objects.get(name='Preceptor') in user.groups.all():
        return True
    return False
