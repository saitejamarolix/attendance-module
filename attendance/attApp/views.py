#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Employee
from datetime import datetime

def check_in(request):
    if request.method == 'POST':
        name = request.POST['name']
        employee = Employee.objects.create(name=name, check_in=datetime.now())
        employee.save()
        return redirect('check_out')
    return render(request, 'check_in.html')

def check_out(request):
    if request.method == 'POST':
        employee = Employee.objects.get(name=request.POST['name'])
        employee.check_out = datetime.now()
        employee.save()
        return redirect('check_in')
    employees = Employee.objects.filter(check_out__isnull=True)
    return render(request, 'check_out.html', {'employees': employees})

def attendance_report(request):
    employees = Employee.objects.all()
    for employee in employees:
        if employee.check_out:
            employee.working_hours = employee.check_out - employee.check_in
        else:
            employee.working_hours = None
    return render(request, 'attendance_report.html', {'employees': employees})