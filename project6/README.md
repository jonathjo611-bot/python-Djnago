# Project 6 - CineBox: multi-app movie site (Django)

## Run (first time)
    pip install django
    python manage.py migrate        # needed for sessions (the watchlist)
    python manage.py runserver
Open http://127.0.0.1:8000/

## Structure (same idea as your spotify project)
- apps: movies, series, watchlist  (each has its own views.py, urls.py, templates)
- templates/base.html   -> navbar + {% block content %}; every page {% extends "base.html" %}
- static/css/style.css  -> loaded in base.html with {% static %}
- project6/urls.py      -> include('movies.urls') under 'movies/', etc.
- movies/data.py, series/data.py -> lists of dicts (no database needed)
- watchlist uses request.session to remember movie ids

## settings.py changes to notice
- INSTALLED_APPS: movies, series, watchlist
- TEMPLATES 'DIRS': [BASE_DIR / 'templates']
- STATICFILES_DIRS = [BASE_DIR / 'static']
