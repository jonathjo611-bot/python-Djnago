# Project 2 - Electricity Bill Calculator (Django)

## Run
    pip install django
    python manage.py runserver
Open http://127.0.0.1:8000/

## Slab rates (edit in bill/views.py)
- first 100 units: Rs 3/unit
- next 100 units:  Rs 5/unit
- next 100 units:  Rs 7/unit
- above 300 units: Rs 9/unit
- plus fixed charge Rs 50

## Files that matter
- bill/forms.py   -> BillForm (plain forms.Form: name, units)
- bill/views.py   -> GET shows form, POST validates + calculates
- bill/urls.py    -> maps '' to bill_view
- bill/templates/bill/1.html -> the form
- bill/templates/bill/2.html -> the result with slab breakdown
