from django import forms
from .models import Appointment
from django.utils import timezone

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'service', 'device_model', 'problem_description', 'appointment_date', 'appointment_time']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date().isoformat()}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
            'problem_description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_appointment_date(self):
        date = self.cleaned_data.get('appointment_date')
        if date < timezone.now().date():
            raise forms.ValidationError("Appointment date cannot be in the past")
        return date 