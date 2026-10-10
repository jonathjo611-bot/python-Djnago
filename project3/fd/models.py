from django.core.validators import MinValueValidator
from django.db import models


class Deposit(models.Model):
    name = models.CharField(max_length=100)
    principal = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    rate = models.FloatField(help_text="Interest rate, % per year",
                             validators=[MinValueValidator(0.1)])
    years = models.FloatField(validators=[MinValueValidator(0.1)])
    created = models.DateTimeField(auto_now_add=True)

    def maturity(self):
        """Compound interest, compounded yearly: P * (1 + r/100) ** t"""
        return round(self.principal * (1 + self.rate / 100) ** self.years, 2)

    def interest(self):
        return round(self.maturity() - self.principal, 2)

    def __str__(self):
        return f"{self.name} - Rs {self.principal}"
