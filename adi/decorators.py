#En este archivo se crean todas las restricciones de acceso 
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import AnonymousUser, User, Group

#Funcion para entrar a la preceptoria
def check_preceptor(user):
    user_groups = user.groups.all()
    if Group.objects.get(name='Padre-Tutor') in user_groups:
        return True
    return False
    
"""
def check_guardia(user):
    user_groups = user.groups.all()
    if Group.objects.get(name='Guardia') in user_groups:
        return True
    return False

def check_padre_tutor(user):
    user_groups = user.groups.all()
    if Group.objects.get(name='Padre-Tutor') in user_groups:
        return True
    return False
"""
