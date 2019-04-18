from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.TextField()
    
    
class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name="patients")
    
# Doctor:Reservation = 1:N
# Patient:Reservation = 1:N
# Doctor:Patient = N:N
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)