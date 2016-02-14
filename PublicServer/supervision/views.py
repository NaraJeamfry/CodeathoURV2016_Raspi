# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render

from django.core.exceptions import ObjectDoesNotExist

from django.views.generic import DetailView

from .models import Classroom, Zone, Faculty, Campus

class ClassroomDetails(DetailView):
    model = Classroom

    def get_object(self, queryset=None):
        campus = self.kwargs.get('campus')
        faculty = self.kwargs.get('faculty')
        zone = self.kwargs.get('zone')
        classroom = self.kwargs.get('classroom')

        if None in (campus, faculty, zone, classroom):
           raise Http404("Falten paràmetres! Torna enrere." )

        try:
            campus = Campus.objects.get(name=campus)
            faculty = Faculty.objects.get(name=faculty, campus=campus)
            zone = Zone.objects.get(name=zone, faculty=faculty)
            classroom = Classroom.objects.get(name=classroom, zone=zone)

            return classroom
        except ObjectDoesNotExist:
            raise Http404("No existeix la classe %s!" % classroom)



class ZoneDetails(DetailView):
    model = Zone

class FacultyDetails(DetailView):
    model = Faculty

class CampusDetails(DetailView):
    model = Campus