from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm

def home(request):
    return render(request, 'appointments/home.html')

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'appointments/appointment_success.html')
def services(request):
    return render(request, 'appointments/services.html')
def about(request):
    return render(request, 'appointments/about.html')