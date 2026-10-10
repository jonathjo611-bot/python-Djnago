from django import forms
from .models import Order


class CheckoutForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)
    phone = forms.RegexField(
        label="Mobile number", regex=r"^[6-9]\d{9}$",
        error_messages={"invalid": "Enter a valid 10-digit mobile number."},
    )
    address = forms.CharField(label="Delivery address", widget=forms.Textarea(attrs={"rows": 3}))
    payment = forms.ChoiceField(label="Payment", choices=Order.PAYMENT, widget=forms.RadioSelect, initial="cod")
