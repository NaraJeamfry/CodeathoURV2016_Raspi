from __future__ import unicode_literals

from django.db import models

from ..faculty.models import Professor
from ..supervision.models import Classroom


class Booking(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    booking_day = models.DateField()


