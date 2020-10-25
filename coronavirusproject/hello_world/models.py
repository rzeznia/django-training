from django.db import models


# Create your models here.
class Person(models.Model):
    sexs = (
        (1, "male"),
        (2, "female"),
        (3, "other"))
    age = models.IntegerField()
    height = models.IntegerField()
    name = models.CharField(max_length=100)
    mass = models.IntegerField()
    sex = models.CharField(max_length=1, choices= sexs)
    email = models.EmailField(blank=True, null=True)
    born_date = models.DateTimeField(auto_now=True, blank=True, null=True)


def __str__(self):
    return f"Osoba: {self.name}, age:{self.age}"
