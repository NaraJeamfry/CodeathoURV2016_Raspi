from __future__ import unicode_literals

from django.db import models


class TimeFrame(models.Model):
    start_hour = models.TimeField()
    end_hour = models.TimeField()

    day = models.DateField()

    class Meta:
        unique_together=('start_hour', 'end_hour', 'day')


class Booking(models.Model):
    professor = models.ForeignKey('faculty.Professor', on_delete=models.CASCADE)
    classroom = models.ForeignKey('supervision.Classroom', on_delete=models.CASCADE)
    frame = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
