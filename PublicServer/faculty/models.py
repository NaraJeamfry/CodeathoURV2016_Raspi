# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User

from supervision.models import Campus, Faculty, Zone, Classroom
from bookings.models import Booking

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Camps del model Usuari per defecte:
    # - is_staff: Té accés al panell d'administració.
    # - username: nom d'usuari
    # - first_name & last_name: nom complert
    # - email: el correu electrònic de l'usuari

    access_campus = models.ManyToManyField(Campus)
    bookings = models.ManyToManyField(Classroom, through=Booking)

    picture = models.ImageField(null=True, default=None)

    class Meta:
        verbose_name = "professor"
        verbose_name_plural = "professors"



