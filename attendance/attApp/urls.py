from django.urls import path
from . import views

urlpatterns = [
    path('check_in/', views.check_in, name='check_in'),
    path('check_out/', views.check_out, name='check_out'),
    path('attendance_report/', views.attendance_report, name='attendance_report'),
]