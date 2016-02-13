from __future__ import unicode_literals

from django.db import models


class Booking(models.Model):
    professor = models.ForeignKey('faculty.Professor', on_delete=models.CASCADE)
    classroom = models.ForeignKey('supervision.Classroom', on_delete=models.CASCADE)
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    booking_day = models.DateField()


