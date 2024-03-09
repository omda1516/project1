from django.db import models
from petient import models as petient_models
from doctor import models as doctor_models


class Refound(models.Model):
    refound_amount=models.DecimalField(max_digits=10, decimal_places=10)





class Reception(models.Model):  
    name= models.CharField(max_length=20)
    refound_id=models.ForeignKey(Refound,on_delete=models.CASCADE)



class Reservation(models.Model):  
    data = models.CharField(max_length=15)
    payment_method= models.CharField(max_length=20)
    payment_amount= models.CharField(max_length=20)
    patientID = models.ForeignKey(petient_models.Patient, on_delete=models.CASCADE,default=1)
    doctorID = models.ForeignKey(doctor_models.Doctor, on_delete=models.CASCADE,default=1)
    refound_id=models.ForeignKey(Refound,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.data} {self.payment_method}"
    


