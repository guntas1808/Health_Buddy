from django.contrib import admin
from .models import HCDept, Day, Prescription, Doctor, PresMedicine

# Register your models here.
admin.site.register(HCDept)
admin.site.register(PresMedicine)
admin.site.register(Day)
admin.site.register(Prescription)
admin.site.register(Doctor)