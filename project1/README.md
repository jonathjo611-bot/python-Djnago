# Project 1 - Student Profile Card (Django)

## Run
    pip install django
    python manage.py runserver
Open http://127.0.0.1:8000/

## Files that matter
- student/views.py   -> data + context dictionary
- student/urls.py    -> maps '' to the view
- project1/urls.py   -> include('student.urls')
- student/templates/student/1.html -> shows {{ name }}, loops over skills
