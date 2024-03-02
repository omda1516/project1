from django.db import models
from django.utils.text import slugify


GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),
]

SHIFT = [
    ("Morning", "Morning"),
    ("Evening", "Evening"),
]


class Patient(models.Model):
    name = models.CharField(max_length=100, unique=True, required=True)
    birth_date = models.DateField()
    national_id_number = models.CharField(max_length=14, unique=True, required=True)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, unique=True, required=True)
    phone_number2 = models.CharField(max_length=20, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, required=True)
    blood_type = models.CharField(max_length=5)
    gender = models.CharField(max_length=6, choices=GENDER)
    specialization = models.ManyToManyField(
        "Specialization", on_delete=models.PROTECT, related_name="specialization"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Patient, self).save(*args, **kwargs)


class Doctor(models.Model):
    name = models.CharField(max_length=100, unique=True, required=True)
    address = models.CharField(max_length=200)
    national_id_number = models.CharField(max_length=14, unique=True, required=True)
    age = models.IntegerField()
    specialization = models.ForeignKey(
        "Specialization", on_delete=models.PROTECT, related_name="specialization"
    )
    phone_number = models.CharField(max_length=20, unique=True, required=True)
    phone_number2 = models.CharField(max_length=20, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, required=True)
    gender = models.CharField(max_length=6, choices=GENDER)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Doctor, self).save(*args, **kwargs)


class Pharmacist(models.Model):
    name = models.CharField(max_length=100, unique=True, required=True)
    address = models.CharField(max_length=200)
    national_id_number = models.CharField(max_length=14, unique=True, required=True)
    shift = models.CharField(max_length=6, choices=SHIFT)
    phone_number = models.CharField(max_length=20, unique=True, required=True)
    phone_number2 = models.CharField(max_length=20, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, required=True)
    gender = models.CharField(max_length=6, choices=GENDER)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Pharmacist, self).save(*args, **kwargs)


class Specialization(models.Model):
    name = models.CharField(max_length=100, unique=True, required=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Specialization, self).save(*args, **kwargs)
