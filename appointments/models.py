from django.db import models
from django.contrib.auth.models import User

# Patient model to store patient details
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patient_profile")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    address = models.TextField(verbose_name="Address")

    def __str__(self):
        return self.user.username


# Services model to store available services
class Service(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Service Name")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")

    def __str__(self):
        return self.name


# Staff model to store staff names and positions
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="staff_profile")
    position = models.CharField(max_length=50, verbose_name="Position")

    def __str__(self):
        return self.user.username


# Appointment model to store appointment details
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    ]

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="appointments",
        default=1  # Replace 1 with a valid Patient ID from your database
    )
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name="appointments")
    date = models.DateField(verbose_name="Appointment Date")
    time = models.TimeField(verbose_name="Appointment Time")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Scheduled', verbose_name="Status")
    notes = models.TextField(blank=True, null=True, verbose_name="Additional Notes")

    def __str__(self):
        return f"{self.patient.user.username} - {self.date} at {self.time}"
