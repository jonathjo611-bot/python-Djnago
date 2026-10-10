# Spotify clone - Section 1: Templates (Django)

Only the Templates section (Q1 - Q7). Styling is internal CSS (<style> inside the templates),
there is no static folder and no logo.

## Run (Windows PowerShell)
    pip install django
    python manage.py runserver
Open http://127.0.0.1:8000/     Run the checks: python manage.py test

## Where each question is answered
| Question | Where |
|---|---|
| Q1 - home.html, <h1>, list of links, render() | templates/home.html, spotifytemplates/views.py |
| Q2 - clickable div cards + internal CSS | templates/home.html (class app-card, <style> in extra_head) |
| Q3 - project base.html, navbar, {% block content %} | templates/base.html (DIRS set in settings.py) |
| Q4 - app-level bases, one colour each | artist/templates/artist/artist.html, playlist/.../playlist.html, podcast/.../podcast.html |
| Q5 - template filters | artist/views.py + artist/templates/artist/artist_detail.html |
| Q6 - {% url %} tags, named paths | every urls.py (name=...) and every template |
| Q7 - loop, forloop.first, if/elif/else, empty | playlist/views.py + playlist/templates/playlist/playlist_detail.html |

## Inheritance chain
base.html (project)  ->  artist/artist.html (app, adds colour)  ->  artist/artist_detail.html (page)
Each level adds its own CSS with {% block extra_head %} (child pages call {{ block.super }} to keep the parent's CSS).

## Testing the empty state (Q7d)
Open http://127.0.0.1:8000/playlist/?empty=1  (the view passes [] instead of the song list)

Artist names, bios and dates are made-up sample data. The playlist is exactly the list from the assignment.
