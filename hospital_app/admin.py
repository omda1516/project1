from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Pharamcy)
admin.site.register(Pharmacist)
admin.site.register(Reception)
admin.site.register(Reservation)
admin.site.register(management)
