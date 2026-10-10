from django import forms
from .models import Deposit


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ["name", "principal", "rate", "years"]
