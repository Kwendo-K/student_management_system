"""
creating database tables
"""
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class StudentRecord(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=200)
    gpa = models.FloatField()

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
