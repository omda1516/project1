# in models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class HospitalUser(AbstractUser):
    GENDERS = [
        ("male", "Male"),
        ("female", "Female"),
    ]
    gender = models.CharField(choices=GENDERS, max_length=20)
