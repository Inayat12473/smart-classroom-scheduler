

# Register your models here.
from django.contrib import admin
from .models import Classroom, Course, Schedule

admin.site.register(Classroom)
admin.site.register(Course)
admin.site.register(Schedule)
