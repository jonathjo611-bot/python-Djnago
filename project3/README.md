# Project 3 - Fixed Deposit Calculator (Django, ModelForm + database)

## Run (first time)
    pip install django
    python manage.py migrate
    python manage.py runserver
Open http://127.0.0.1:8000/   (history at /history/)

## Flow: model -> form -> view -> url -> template
- fd/models.py  -> Deposit (+ maturity() and interest() methods)
- fd/forms.py   -> DepositForm (ModelForm, no field repeated by hand)
- fd/views.py   -> calculate (validate, save, show result), history (read from DB)
- fd/templates/fd/1.html form | 2.html result | 3.html history
Admin: python manage.py createsuperuser, then open /admin/
