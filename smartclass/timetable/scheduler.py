from .models import Course, Classroom, Schedule
from accounts.models import Profile

DAYS = ['Mon','Tue','Wed','Thu','Fri']
TIME_SLOTS = ['9:00-10:00','10:00-11:00','11:00-12:00','1:00-2:00','2:00-3:00']

def generate_timetable():
    courses = Course.objects.all()
    teachers = Profile.objects.filter(role='teacher')
    classrooms = Classroom.objects.all()
    
    # Clear old schedule
    Schedule.objects.all().delete()

    for course in courses:
        hours_needed = course.hours_per_week
        count = 0
        for day in DAYS:
            for slot in TIME_SLOTS:
                if count >= hours_needed:
                    break

                # Check available teacher
                available_teacher = None
                for t in teachers:
                    if not Schedule.objects.filter(teacher=t, day=day, time_slot=slot).exists():
                        available_teacher = t
                        break
                if not available_teacher:
                    continue  # skip if no teacher available

                # Check available classroom
                available_classroom = None
                for c in classrooms:
                    if not Schedule.objects.filter(classroom=c, day=day, time_slot=slot).exists():
                        available_classroom = c
                        break
                if not available_classroom:
                    continue  # skip if no classroom available

                # Create schedule entry
                Schedule.objects.create(
                    course=course,
                    teacher=available_teacher,
                    classroom=available_classroom,
                    day=day,
                    time_slot=slot
                )
                count += 1

    print("Timetable Generated Successfully!")
