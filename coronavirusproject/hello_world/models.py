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
    sex = models.IntegerField(choices=sexs)
    email = models.EmailField(blank=True, null=True)
    born_date = models.DateTimeField(auto_now=True, blank=True, null=True)


    def cal_cal(self):
        if self.sex == "1":
            return 66.47 + 13.7 * self.mass + 5.0 * self.height - 6.76 * self.age
        if self.sex == "2":
            return 655.1 + 9.567 * self.mass + 1.85 * self.height - 4.68 * self.age
        else:
            return "Nie da sie"

    def __str__(self):
        return f"Osoba: {self.name}, age:{self.age}"



