from django.db import models
from django.urls import reverse
from django.core.validators import MaxLengthValidator,MinLengthValidator
from enum import Enum

# Create your models here.
class Student(models.Model):
    EducationStatus = (
        ('m4', 'ม4'),
        ('m5', 'ม5'),
        ('m6', 'ม6'),
        ('mx', 'อื่นๆ'),
    )


    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    personalID = models.CharField(max_length = 13, validators=[MaxLengthValidator(13), MinLengthValidator(13)])
    # education =  models.CharField(max_length=10)
    education = models.CharField(max_length=2,choices=EducationStatus,default='mx')

    # school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

