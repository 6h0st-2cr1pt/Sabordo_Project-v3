from django.db import models
from django.utils import timezone

# Create your models here.

class Appointment(models.Model):
    SERVICE_CHOICES = [
        ('screen_repair', 'Screen Repair'),
        ('battery_replacement', 'Battery Replacement'),
        ('water_damage', 'Water Damage Repair'),
        ('malware_removal', 'Malware Removal'),
        ('board_repair', 'Board Repair'),
        ('data_recovery', 'Data Recovery'),
        ('phone_check_up', 'Phone Check Up'),
        ('hardware_upgrade', 'Hardware Upgrade'),
        ('hardware_replacement', 'Hardware Replacement'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    device_model = models.CharField(max_length=100)
    problem_description = models.TextField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.service} - {self.appointment_date}"

    class Meta:
        ordering = ['-appointment_date', '-appointment_time']
