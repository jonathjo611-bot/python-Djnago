from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

MARK = [MinValueValidator(0), MaxValueValidator(100)]


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    maths = models.IntegerField(validators=MARK)
    science = models.IntegerField(validators=MARK)
    english = models.IntegerField(validators=MARK)

    def total(self):
        return self.maths + self.science + self.english

    def percentage(self):
        return round(self.total() / 3, 2)

    def grade(self):
        p = self.percentage()
        if p >= 90:
            return "A+"
        elif p >= 80:
            return "A"
        elif p >= 70:
            return "B"
        elif p >= 60:
            return "C"
        elif p >= 50:
            return "D"
        return "F"

    def __str__(self):
        return f"{self.roll_no} - {self.name}"
