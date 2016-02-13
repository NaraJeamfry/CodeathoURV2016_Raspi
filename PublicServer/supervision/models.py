# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Classroom_Properties(models.Model):
    name = models.CharField(max_length=24)
    has_count = models.BooleanField()


class Campus(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    director = models.ForeignKey(User, on_delete=models.SET_NULL)


class Faculty(models.Model):
    name = models.CharField(max_length=32)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    director = models.ForeignKey(User, on_delete=models.SET_NULL)


class Zone(models.Model):
    name = models.CharField(max_length=16)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class Classroom(models.Model):
    LABORATORI='LAB'
    TEORIA='TEO'
    INFORMATICA='INF'
    EXAMEN='EXA'
    TYPES = (
        ('Generals', ((TEORIA, 'Aula teoria'),(EXAMEN, 'Aula d\'examen'),) ),
        (
            'Específics',
            (
                (LABORATORI, 'Laboratori'),
                (INFORMATICA, 'Aula d\'informàtica'),
            )
        ),
    )
    # Limitem el nom per evitar noms kilometrics
    name = models.CharField(max_length=32)

    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=TYPES, default=TEORIA)

    properties = models.ManyToManyField(Classroom_Properties)
