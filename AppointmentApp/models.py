from django.db import models
from AccountApp.models import doctor, Patient

class Status(models.TextChoices):
    PENDING = 'pending', 'Pending'
    CONFIRMED = 'confirmed', 'Confirmed'
    COMPLETED = 'completed', 'Completed'
    CANCELLED = 'cancelled', 'Cancelled'

class Appointment(models.Model):
    reason = models.TextField()
    prescription = models.FileField(upload_to='prescriptions/', null=True, blank=True)
    duration = models.PositiveIntegerField(default=30)  # Duration in minutes
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=Status.choices, default=Status.PENDING)
    doctor = models.ForeignKey('AccountApp.doctor', on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey('AccountApp.Patient', on_delete=models.CASCADE, related_name='appointments')

    
    
   
