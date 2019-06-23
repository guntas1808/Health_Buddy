from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.
class Reception(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)