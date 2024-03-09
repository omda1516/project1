# # in models.py
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
# from django.db import models


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractUser, PermissionsMixin):
#     # Add custom fields here
#     # For example:
#     age = models.IntegerField(null=True, blank=True)
#     GENDERS = [
#         ("male", "Male"),
#         ("female", "Female"),
#     ]
#     gender = models.CharField(choices=GENDERS, max_length=20)
#     is_patient = models.BooleanField(default=False)
#     is_doctor = models.BooleanField(default=False)
#     is_receptionist = models.BooleanField(default=False)
#     is_pharmacist = models.BooleanField(default=False)
#     is_management = models.BooleanField(default=False)


# # class Patient(models.Model):
# #     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)



# #     USERNAME_FIELD = 'email'
# #     REQUIRED_FIELDS = ['first_name', 'last_name']



# class Patient(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     # Add more fields specific to patients, such as age, gender, medical history, etc.

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)


#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,AbstractUser
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser, PermissionsMixin):
    # Add custom fields here
    # For example:
    age = models.IntegerField(null=True, blank=True)
    GENDERS = [
        ("male", "Male"),
        ("female", "Female"),
    ]
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    gender = models.CharField(choices=GENDERS, max_length=20)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_receptionist = models.BooleanField(default=False)
    is_pharmacist = models.BooleanField(default=False)
    is_management = models.BooleanField(default=False)

    objects = CustomUserManager()

class Patient(CustomUser):
    # Add more fields specific to patients, such as age, gender, medical history, etc.
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
