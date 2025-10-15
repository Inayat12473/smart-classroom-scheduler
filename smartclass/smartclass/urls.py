from django.contrib import admin
from django.urls import path, include
from main import views as main_views  # ✅ import your home view from main app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),  # ✅ this is your real homepage
    path('accounts/', include('accounts.urls')),
    path('timetable/', include('timetable.urls')),
    path('', include('main.urls')),
]
