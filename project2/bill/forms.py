from django import forms


class BillForm(forms.Form):
    name = forms.CharField(label="Customer name", max_length=100)
    units = forms.IntegerField(label="Units consumed", min_value=0)
