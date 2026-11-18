from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import  MinLengthValidator,RegexValidator  

class User(AbstractUser):

    pass
class Specialist(models.Model):
    name = models.CharField(max_length=100)
    
   

class doctor(User):
    license_number = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6), RegexValidator(r'^\d{6}$', 'License number must be exactly 6 digits.')])
    phone = models.CharField(max_length=8, validators=[MinLengthValidator(8), RegexValidator(r'^\d{8}$', 'Phone number must be exactly 8 digits.')])
    specialist = models.ManyToManyField('Specialist', related_name='doctors')

class Patient(User):
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15, validators=[MinLengthValidator(15), RegexValidator(r'^\d{15}$', 'Phone number must be exactly 15 digits.')])
    national_id = models.CharField(max_length=20, unique=True)
   
   
