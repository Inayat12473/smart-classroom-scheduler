# Create your views here.
from django.shortcuts import render, redirect
from .models import Course, Classroom, Schedule
from .scheduler import generate_timetable  # <-- import your scheduler function

# View to display the timetable
def view_timetable(request):
    schedule = Schedule.objects.all()
    return render(request, 'timetable/view_timetable.html', {'schedule': schedule})

# View to generate the timetable
def generate_timetable_view(request):
    generate_timetable()  # <-- call your scheduler function
    return redirect('view_timetable')  # <-- redirect to the timetable view
