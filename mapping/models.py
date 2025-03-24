from django.db import models
from patients.models import Patient
from doctor.models import Doctor
# Create your models here.
class Mapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Mapping: Patient {self.patient.name} - Doctor {self.doctor.name}"