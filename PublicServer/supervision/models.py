# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from classroom_server.raspberry import get_status, test_connection


class ClassroomProperties(models.Model):
    name = models.CharField(max_length=24)
    has_count = models.BooleanField()

    display_name = models.CharField(max_length=32, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "property"
        verbose_name_plural = "properties"
        ordering = ['name']


class Campus(models.Model):
    name = models.CharField(max_length=32, unique=True)
    address = models.CharField(max_length=128)
    director = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "campus"
        verbose_name_plural = "campuses"
        ordering = ['name']


class Faculty(models.Model):
    name = models.CharField(max_length=32)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    director = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "faculty"
        verbose_name_plural = "faculties"
        ordering = ['name']


class Zone(models.Model):
    name = models.CharField(max_length=16)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __unicode__(self):
        return "{} ({})".format(self.name, self.faculty.name)

    class Meta:
        verbose_name = "zone"
        verbose_name_plural = "zones"
        ordering = ['name']


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

    raspberry_pi_ip = models.GenericIPAddressField(blank=True, null=True, default=None)

    photo = models.ImageField(null=True, blank=True, default=None)

    properties = models.ManyToManyField(ClassroomProperties)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "classroom"
        verbose_name_plural = "classrooms"
        ordering = ['name']

    def get_current_status(self):
        if self.raspberry_pi_ip is None:
            return {"Raspberry": "No configurat"}
        classroom = {}

        can_connect = test_connection(self.raspberry_pi_ip)

        if not can_connect:
            return {"Raspberry": "APAGAT"}
        else:
            classroom = {"Raspberry": "CONNECTAT"}

        for property in self.properties.all():
            status = get_status(self.raspberry_pi_ip, property.name)
            classroom.update({property: status})

        return classroom

