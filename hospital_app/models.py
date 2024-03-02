from django.db import models


class Patient(models.Model):
    GENDER_TABLE =(
        ('M', 'Male'),
        ('F', 'Female'),
    )
    BLOOD_TABLE=(
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_TABLE)
    blood = models.CharField(max_length=3, choices=BLOOD_TABLE)
    patient_status = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Pharamcy(models.Model):  
    contact_number = models.CharField(max_length=15)
    location= models.CharField(max_length=20)
    name= models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.location}"



class Doctor(models.Model):  
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    doctor_price= models.CharField(max_length=15)
    university= models.CharField(max_length=30)
    specialty= models.CharField(max_length=20)
    pharmacyID = models.ForeignKey(Pharamcy, on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"




class Pharmacist(models.Model):  
    contact_number = models.CharField(max_length=15)
    name= models.CharField(max_length=20)
    pharmacyID = models.ForeignKey(Pharamcy, on_delete=models.CASCADE,default=1)
    def __str__(self):
        return f"{self.name} {self.location}"
    



class Refound(models.Model):
    refound_amount=models.DecimalField(max_digits=10, decimal_places=10)





class Reception(models.Model):  
    name= models.CharField(max_length=20)
    refound_id=models.ForeignKey(Refound,on_delete=models.CASCADE)



class Reservation(models.Model):  
    data = models.CharField(max_length=15)
    payment_method= models.CharField(max_length=20)
    payment_amount= models.CharField(max_length=20)
    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE,default=1)
    doctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE,default=1)
    refound_id=models.ForeignKey(Refound,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.data} {self.payment_method}"
    



class management(models.Model):  
    name = models.CharField(max_length=15)

        
    doctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE,default=1)
    refound_id=models.ForeignKey(Refound,on_delete=models.CASCADE)
    Patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Reception_id=models.ForeignKey(Reception,on_delete=models.CASCADE)
    Pharamcy_id=models.ForeignKey(Pharamcy,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    
    # doctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE,default=1)
    # refound_id=models.ForeignKey(Refound,on_delete=models.CASCADE)
    # Patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE)
    # Reception_id=models.ForeignKey(Reception,on_delete=models.CASCADE)
    # Pharamcy_id=models.ForeignKey(Pharamcy,on_delete=models.CASCADE)