# Project 5 - Library Manager (Django admin + search + detail pages)

## Run (first time)
    pip install django
    python manage.py migrate
    python manage.py loaddata books        # adds 6 sample books
    python manage.py createsuperuser       # pick any username/password
    python manage.py runserver
- Site:  http://127.0.0.1:8000/   (try /?q=narayan)
- Admin: http://127.0.0.1:8000/admin/  (add, edit and delete books here)

## New ideas compared to project 4
- the admin site (admin.py) instead of writing your own add/edit pages
- request.GET for search, filter(title__icontains=...)
- path('book/<int:id>/') + get_object_or_404 for a detail page
- fixtures: sample data in a JSON file, loaded with loaddata
