from django.contrib import admin

from .models import *

admin.site.register(Campus)
admin.site.register(Faculty)
admin.site.register(Zone)

admin.site.register(ClassroomProperties)

admin.site.register(Classroom)
