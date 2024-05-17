from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator


# Create your models here.

class appForm(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    COURSE_CHOICES = [('--Select--', '--Select--'), ('Option1', 'Option1')]
    ENTRY_SCHEME_CHOICES = [('--Select--', '--Select--'), ('Option1', 'Option1')]
    INTAKE_CHOICES = [('--Select--', '--Select--'), ('Option1', 'Option1')]
    SPONSORSHIP_CHOICES = [('--Select--', '--Select--'), ('Option1', 'Option1')]
    first_name = models.CharField(validators=[MinLengthValidator(2)], max_length=255)
    last_name = models.CharField(validators=[MinLengthValidator(2)], max_length=255)
    course = models.CharField(validators=[MinLengthValidator(2)], max_length=255, choices=COURSE_CHOICES)
    entry_scheme = models.CharField(validators=[MinLengthValidator(2)], max_length=255, choices=ENTRY_SCHEME_CHOICES)
    intake = models.CharField(validators=[MinLengthValidator(2)], max_length=100, choices=INTAKE_CHOICES)
    sponsorship = models.CharField(validators=[MinLengthValidator(2)], max_length=100, choices=SPONSORSHIP_CHOICES)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(validators=[MinLengthValidator(2)], max_length=255)
    residence = models.CharField(validators=[MinLengthValidator(2)], max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name
    





