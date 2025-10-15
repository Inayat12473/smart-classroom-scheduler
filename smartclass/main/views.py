from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'main/home.html')

@login_required(login_url='/accounts/login/')
def dashboard(request):
    return render(request, 'main/dashboard.html')

@login_required(login_url='/accounts/login/')
def view_timetable(request):
    return render(request, 'timetable/view.html')

@login_required(login_url='/accounts/login/')
def generate_timetable(request):
    return render(request, 'timetable/generate.html')
