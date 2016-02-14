from __future__ import unicode_literals

from django.db import models


class Frame(models.Model):
    start_hour = models.TimeField()
    end_hour = models.TimeField()


class TimeFrame(models.Model):
    frame = models.ForeignKey(Frame)

    day = models.DateField()

    class Meta:
        unique_together=('frame', 'day')


class Booking(models.Model):
    professor = models.ForeignKey('faculty.Professor', on_delete=models.CASCADE)
    classroom = models.ForeignKey('supervision.Classroom', on_delete=models.CASCADE)
    frame = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)

    class Meta:
        unique_together=(('classroom', 'frame'),)
