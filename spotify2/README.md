# Spotify (improved) - Django mini music site

Same three apps as your spotify1 project (artist, playlist, podcast), now with a database,
detail pages, search, a "Liked songs" list and a real stylesheet.

## Run (first time) - Windows PowerShell
    pip install django
    python manage.py migrate
    python manage.py loaddata sample_data
    python manage.py createsuperuser
    python manage.py runserver
- Site:  http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/   (add artists, songs, playlists, podcasts and episodes)
- Tests: python manage.py test

The sample data (artists, songs, play counts, podcasts) is for practice. Numbers are invented.

## What is new compared to spotify1
| Your spotify1                      | This version                                              |
|------------------------------------|-----------------------------------------------------------|
| Lists of dicts typed in views.py   | Models + database (Artist, Song, Playlist, Podcast, Episode) |
| One page per app                   | List page + detail page (artist/<int:id>/ etc.)           |
| CSS written inside templates       | One stylesheet: static/css/spotify.css                    |
| Nav links only                     | Active-page highlight + search box                        |
| Songs printed as 3 separate lists  | One reusable table: templates/partials/song_table.html    |
| -                                  | ForeignKey (Song -> Artist) and ManyToMany (Playlist <-> Song) |
| -                                  | Liked songs remembered with request.session               |

## Template filters used (you used some already)
title, upper, default, length-style counts, date, slice, truncatewords, pluralize, intcomma, add, urlencode

## Where to look
- artist/models.py, playlist/models.py, podcast/models.py   -> the data
- */views.py and */urls.py                                  -> logic and links
- templates/base.html                                       -> navbar shared by all pages
- spotify2/views.py                                         -> home page and search
