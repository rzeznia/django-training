from django.db import models

# Create your models here.
class Person(models.Model):
    age = models.IntegerField()
    height = models.IntegerField()
    name = models.CharField(max_length=100)
    mass = models.IntegerField()
    sex = models.CharField(max_length=10)