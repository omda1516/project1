from django.db import models
from pharamcy import models as pharamcy_models


class Doctor(models.Model):  
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    doctor_price= models.CharField(max_length=15)
    university= models.CharField(max_length=30)
    specialty= models.CharField(max_length=20)
    pharmacyID = models.ForeignKey(pharamcy_models.Pharamcy, on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
