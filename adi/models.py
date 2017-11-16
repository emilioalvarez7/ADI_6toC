#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import string
import random
from django.contrib.auth.models import User, Group
from django.conf import settings

# Create your models here.

class Tutor(models.Model):
    nombre = models.CharField('Nombre', max_length=25)
    apellido = models.CharField('Apellido', max_length=25)
    dni = models.PositiveIntegerField('DNI', primary_key=True)
    email = models.CharField('Dirección e-mail', max_length=50, null=True)
    num_cel = models.CharField('Número de celular', max_length=14, null=True)
    nombre_usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    grupo_usuario = models.ForeignKey(Group)

    class Meta:
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'

    def __str__(self):
        return '{} {} DNI: {}'.format(self.nombre, self.apellido, self.dni)

    def generarCodigoComoFirma(maximo=5, caracteres=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(caracteres) for i in range(maximo))

    codigo_como_firma = models.CharField('Firma', unique=True, max_length=5, default=generarCodigoComoFirma())

class Preceptor(models.Model):
    nombre = models.CharField('Nombre', max_length=25)
    apellido = models.CharField('Apellido', max_length=25)
    dni = models.PositiveIntegerField('DNI', primary_key=True)
    num_cel = models.CharField('Número de celular', max_length=14, null=True)
    email = models.EmailField('Dirección e-mail', max_length=100, null=True)
    nombre_usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    grupo_usuario = models.ForeignKey(Group)

    class Meta:
        verbose_name = 'Preceptor'
        verbose_name_plural = 'Preceptores'

    def __str__(self):
        return '{} {} DNI.: {}'.format(self.nombre, self.apellido, self.dni)

class Curso(models.Model):
    PRIMERO = 1
    SEGUNDO = 2
    TERCERO = 3
    CUARTO = 4
    QUINTO = 5
    SEXTO = 6
    SEPTIMO = 7

    A = 'A'
    B = 'B'
    C = 'C'

    ANUARIO_CHOICES = (
        (PRIMERO, '1'),
        (SEGUNDO, '2'),
        (TERCERO, '3'),
        (CUARTO, '4'),
        (QUINTO, '5'),
        (SEXTO, '6'),
        (SEPTIMO, '7')
    )

    DIVISION_CHOICES = (
        (A, 'A'),
        (B, 'B'),
        (C, 'C')
    )
    anuario = models.PositiveSmallIntegerField('Año', choices=ANUARIO_CHOICES)
    division = models.CharField('División', max_length=1, choices=DIVISION_CHOICES)
    preceptor = models.ForeignKey(Preceptor, on_delete=models.CASCADE, related_name='cursos')

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return '{} Año {}'.format(self.anuario, self.division)

"""
class Asistencia(models.Model):

    TIPO_CHOICES = (
        (True, 'Justificada'),
        (False, 'Injustificada'),
    )

    VALOR_CHOICES = (
        (0.25, '1/4'),
        (0.50, '1/2'),
        (1, '1')
    )

    tipo = models.BooleanField(choices=TIPO_CHOICES)
    valor = models.CharField(choices=VALOR_CHOICES)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='inasistencias')
"""
class Alumno(models.Model):
    PRESENTE = 'PR'
    AUSENTE = 'AU'
    RETIRADO = 'RE'
    LLEGO_TARDE = 'TA'
    NO_DEFINIDO = 'ND'

    ESTADO_CHOICES = (
        (PRESENTE, 'Presente'),
        (AUSENTE, 'Ausente'),
        (RETIRADO, 'Retirado'),
        (LLEGO_TARDE, 'Llegó tarde'),
        #Para la primera vez que se carga
        (NO_DEFINIDO, 'Indefinido'),
    )

    nombre = models.CharField('Nombre', max_length=25)
    apellido = models.CharField('Apellido', max_length=25)
    dni = models.PositiveIntegerField('DNI', primary_key=True)
    legajo = models.PositiveSmallIntegerField('Legajo', unique=True, null=True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', null=True)
    direccion = models.CharField('Calle', max_length=100, null=True)
    foto = models.ImageField('Foto', upload_to='adi/static/media/img/fotos_alumnos/', max_length=60, null=True)
    inasistencias_justificadas = models.DecimalField('Inasistencias Justificadas', max_digits=2, decimal_places=2, default=0.0)
    inasistencias_injustificadas = models.DecimalField('Inasistencias Injustificadas', max_digits=2, decimal_places=2, default=0.0)
    estado = models.CharField('Estado', max_length=2, choices=ESTADO_CHOICES, default=ESTADO_CHOICES[4])
    observaciones = models.PositiveSmallIntegerField('Observaciones', default=0)
    amonestaciones = models.PositiveSmallIntegerField('Amonestaciones', default=0)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='hijos')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='alumnos')
    nombre_usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    grupo_usuario = models.ForeignKey(Group)

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def __str__(self):
        return '{} {} DNI.: {}'.format(self.nombre, self.apellido, self.dni)

    def aplicarObservacion(self):
        self.observaciones += 1
        self.save()
        #Intentar amonestar
        if (self.observaciones > 13):
            self.observaciones = 0
            self.amonestaciones += 1
            self.save()
            return self.amonestaciones and self.observaciones
        else:
            return self.observaciones

    def getTotalInasistencias(self):
        return (self.inasistencias_justificadas + self.inasistencias_injustificadas)

class Guardia(models.Model):
    nombre = models.CharField('Nombre', max_length=25)
    apellido = models.CharField('Apellido', max_length=25)
    dni = models.PositiveIntegerField(primary_key=True)
    num_cel = models.CharField('Número de celular', max_length=14, null=True)
    nombre_usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    grupo_usuario = models.ForeignKey(Group)

    class Meta:
        verbose_name = 'Guardia'
        verbose_name_plural = 'Guardias'

    def __str__(self):
        return '{} {} DNI: {}'.format(self.nombre, self.apellido, self.dni)

class Formulario(models.Model):
    FORMULARIO_1 = 'F1'
    FORMULARIO_2 = 'F2'
    FORMULARIO_3 = 'F3'

    FORMULARIO_CHOICES = (
        (FORMULARIO_1, 'Formulario 1'),
        (FORMULARIO_2, 'Formulario 2'),
        (FORMULARIO_3, 'Formulario 3')
    )

    ESTADO_COICES = (
        (True, 'Entregado'),
        (False, 'No entregado'),
    )

    tipo_formulario = models.CharField('Tipo de formulario', max_length=2, choices=FORMULARIO_CHOICES)
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    motivo = models.CharField('Motivo', max_length=254, null=True)
    estado = models.CharField('Estado', max_length=2, choices=ESTADO_COICES, default=ESTADO_COICES[1], null=True)
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE, related_name="alumno")
    guardia = models.ForeignKey(Guardia, on_delete=models.CASCADE, related_name="formularios")

    class Meta:
        verbose_name = 'Formulario'
        verbose_name_plural = 'Formularios'

    def __str__(self):
        return '{} de {} para {}'.format(self.tipo_formulario, self.alumno.curso.preceptor, self.alumno)
