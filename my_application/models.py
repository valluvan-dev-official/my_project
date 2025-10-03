from django.db import models

# Create your models here.


class Sample_data(models.Model):

    student_name = models.CharField(max_length=30)
    student_class = models.CharField(max_length=25)
    address = models.CharField(max_length=200)

    

class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()