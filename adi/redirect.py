from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from .models import *
from .decorators import *

#El user_passes_test sirve para que si la funcion check_preceptor devuelve True sigue , sino corre el login_url='login_p'.
@user_passes_test(check_Preceptor)
def preceptor(request):
    return render (request, 'preceptor/index.html')

#@user_passes_test(check_guardia, login_url='/')
def index_guardia(request):
    print "entra"
    return render(request, 'guardia/index.html')

def cpreceptor(request):
    return render(request, 'admin/crear_preceptor.html')

def chalumno(request):
    return render(request, 'admin/modificar_alumno.html')

def calumno(request):
    return render(request, 'admin/cargar_alumno.html')

def guardia(request):
    return render(request, 'guardia.html')

def inicio(request):
    return render(request, 'inicio.html')

def login_p(request):
    return render(request, 'login.html')

#DIRECTOR
@user_passes_test(check_Director)
def director(request):
    print 'VISTA DEL DIRECTOR'
    grupos = Group.objects.all()
    cursos = Curso.objects.all()
    preceptores = Preceptor.objects.all().order_by('nombre', 'apellido', 'cursos__anuario', 'cursos__division')
    return render(
        request,
        'admin/director.html',
        {'todos_los_preceptores': preceptores,
        'todos_los_grupos': grupos,
        'todos_los_cursos': cursos}
)
