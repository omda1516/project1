from django.db import models

class Pharamcy(models.Model):  
    contact_number = models.CharField(max_length=15)
    location= models.CharField(max_length=20)
    name= models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.location}"
    
    
    
    
class Pharmacist(models.Model):  
    contact_number = models.CharField(max_length=15)
    name= models.CharField(max_length=20)
    pharmacyID = models.ForeignKey(Pharamcy, on_delete=models.CASCADE,default=1)
    def __str__(self):
        return f"{self.name} {self.location}"
