from django.db import models

# Create your models here.
class Registro(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=245)
    password = models.CharField(max_length=50)