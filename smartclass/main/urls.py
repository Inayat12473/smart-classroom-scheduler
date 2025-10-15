# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # home view you just added
    path('dashboard/', views.dashboard, name='dashboard'),
]
