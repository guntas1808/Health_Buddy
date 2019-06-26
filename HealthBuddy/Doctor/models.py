from django.db import models
from django.contrib.auth.models import Permission, User
from Pharmacy.models import Medicine
# from seven.models import Test
#from users.models import Test

# Create your models here.
class HCDept(models.Model):
    deptName = models.CharField(max_length=50)

    def __str__(self):
        return self.deptName

class Test(models.Model):
    test = models.CharField(max_length=100)

    def __str__(self):
        return self.test


class Day(models.Model):
    day = models.CharField(max_length=10)

    def __str__(self):
        return self.day

class Timing(models.Model):
    timing = models.CharField(max_length= 10)

    def __str__(self):
        return self.timing

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    department = models.ForeignKey(HCDept, on_delete=models.CASCADE)
    roomNo = models.CharField(max_length=15)
    visitDays = models.ManyToManyField(Day)
    #timings = models.ForeignKey(Timing, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username


class Prescription(models.Model):
    date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medicines = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    remarks = models.TextField(blank=True)
    tests = models.ForeignKey(Test, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.id



