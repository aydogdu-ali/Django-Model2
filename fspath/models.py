from django.db import models


class Student(models.Model):
    first_name= models.CharField(max_length=30)# chardfield data tipidir.max_length= parametresi zorunludur.
    last_name = models.CharField(max_length=40)
    number = models.PositiveIntegerField(blank=True) # pozitif ve 32767 ye kadar gider.
