# Project 4 - Student Marks & Grade Manager (Django)

## Run (first time)
    pip install django
    python manage.py migrate
    python manage.py runserver
Open http://127.0.0.1:8000/  (results at /list/)

## New ideas compared to project 3
- redirect('list') after saving, and {% url 'list' %} in templates (named URLs)
- validators on the model (marks must be 0-100)
- model methods: total(), percentage(), grade() used directly in the template
- delete with <int:id> in the URL + get_object_or_404, POST only
