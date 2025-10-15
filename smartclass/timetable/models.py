

# Create your models here.
from django.db import models
from accounts.models import Profile
  # correct import


# Classroom model
class Classroom(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    room_type = models.CharField(max_length=20, choices=(('theory','Theory'), ('lab','Lab')))

    def __str__(self):
        return self.name

# Course model
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    hours_per_week = models.IntegerField()

    def __str__(self):
        return self.name

# Schedule model
class Schedule(models.Model):
    DAYS = (
        ('Mon','Monday'),
        ('Tue','Tuesday'),
        ('Wed','Wednesday'),
        ('Thu','Thursday'),
        ('Fri','Friday'),
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Profile, limit_choices_to={'role':'teacher'}, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    day = models.CharField(max_length=3, choices=DAYS)
    time_slot = models.CharField(max_length=20)  # e.g., "9:00-10:00"

    def __str__(self):
        return f"{self.course} - {self.day} - {self.time_slot}"
