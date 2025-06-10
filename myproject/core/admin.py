from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'appointment_date', 'appointment_time', 'status')
    list_filter = ('service', 'status', 'appointment_date')
    search_fields = ('name', 'email', 'phone', 'device_model')
    date_hierarchy = 'appointment_date'
    ordering = ('-appointment_date', '-appointment_time')
