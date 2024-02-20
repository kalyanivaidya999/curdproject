from django.db import models

# Create your models here.
class datasheet(models.Model):
    emp_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    salary = models.CharField(max_length=100)