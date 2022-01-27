from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    f_name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    total_marks=models.IntegerField()
    status=models.BooleanField()
