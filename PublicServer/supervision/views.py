# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

import datetime

from django.db.models import F
from django.http import Http404
from django.shortcuts import render

from django.core.exceptions import ObjectDoesNotExist

from django.views.generic import DetailView, ListView

from .models import Classroom, Zone, Faculty, Campus

from bookings.models import TimeFrame, Booking, Frame


class ListCampus(ListView):
    model = Campus


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

    def get_context_data(self, **kwargs):
        context = super(ClassroomDetails, self).get_context_data(**kwargs)

        context['status'] = self.object.get_current_status()

        return context



class ZoneDetails(DetailView):
    model = Zone

    def get_object(self, queryset=None):
        campus = self.kwargs.get('campus')
        faculty = self.kwargs.get('faculty')
        zone = self.kwargs.get('zone')

        if None in (campus, faculty, zone):
           raise Http404("Falten paràmetres! Torna enrere." )

        try:
            campus = Campus.objects.get(name=campus)
            faculty = Faculty.objects.get(name=faculty, campus=campus)
            zone = Zone.objects.get(name=zone, faculty=faculty)

            return zone
        except ObjectDoesNotExist:
            raise Http404("No existeix la classe %s!" % zone)

class FacultyDetails(DetailView):
    model = Faculty

    def get_object(self, queryset=None):
        campus = self.kwargs.get('campus')
        faculty = self.kwargs.get('faculty')

        if None in (campus, faculty):
           raise Http404("Falten paràmetres! Torna enrere." )

        try:
            campus = Campus.objects.get(name=campus)
            faculty = Faculty.objects.get(name=faculty, campus=campus)

            return faculty
        except ObjectDoesNotExist:
            raise Http404("No existeix la classe %s!" % faculty)

class CampusDetails(DetailView):
    model = Campus

    def get_object(self, queryset=None):
        campus = self.kwargs.get('campus')

        if campus is None:
           raise Http404("Falten paràmetres! Torna enrere." )

        try:
            campus = Campus.objects.get(name=campus)

            return campus
        except ObjectDoesNotExist:
            raise Http404("No existeix la classe %s!" % campus)