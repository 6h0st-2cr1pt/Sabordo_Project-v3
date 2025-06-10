from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointment

def home(request):
    return render(request, 'main.html')

def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            messages.success(request, 'Your appointment has been scheduled successfully! We will contact you shortly to confirm.')
            return redirect('home')
    else:
        form = AppointmentForm()
    
    return render(request, 'schedule.html', {'form': form})
