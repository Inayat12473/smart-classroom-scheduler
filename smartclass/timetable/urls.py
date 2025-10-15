from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view_timetable, name='view_timetable'),
    path('generate/', views.generate_timetable_view, name='generate_timetable'),
]

