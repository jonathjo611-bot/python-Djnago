# Spotify clone - Section 1 (Templates) + Section 2 (Static Files)  (Django)

## Run (Windows PowerShell)
    pip install django
    python manage.py runserver
Open http://127.0.0.1:8000/     Run the checks: python manage.py test

## What Section 2 changed
| Question | What was done |
|---|---|
| Static Q1 | Created static/css/style.css and moved ALL the internal <style> CSS into it. base.html now has {% load static %} and <link rel="stylesheet" href="{% static 'css/style.css' %}">. |
| Static Q2 | Added static/images/logo.png and shows it in the navbar: <img src="{% static 'images/logo.png' %}" alt="App Logo"> |
| settings.py | STATIC_URL = 'static/' (already there) and STATICFILES_DIRS = [BASE_DIR / 'static'] (added) |

## Because the CSS moved
- The page templates no longer use {% block extra_head %} with <style> tags.
- The per-app colours now come from CSS classes in style.css:
  .artist-theme (purple), .playlist-theme (teal), .podcast-theme (orange).
  Each app-level base template just adds that class to its <section>.

## Where each Section 1 question is answered
| Question | Where |
|---|---|
| Q1 - home.html, <h1>, list of links, render() | templates/home.html, spotifytemplates/views.py |
| Q2 - clickable div cards | templates/home.html (class app-card), styled in static/css/style.css |
| Q3 - project base.html, navbar, {% block content %} | templates/base.html (DIRS set in settings.py) |
| Q4 - app-level bases, one colour each | artist/artist.html, playlist/playlist.html, podcast/podcast.html |
| Q5 - template filters | artist/views.py + artist/templates/artist/artist_detail.html |
| Q6 - {% url %} tags, named paths | every urls.py (name=...) and every template |
| Q7 - loop, forloop.first, if/elif/else, empty | playlist/views.py + playlist/templates/playlist/playlist_detail.html |

## Testing the empty state (Q7d)
Open http://127.0.0.1:8000/playlist/?empty=1

The logo is an original design (green circle with sound bars). Replace static/images/logo.png to use your own.
Artist names, bios and dates are made-up sample data.
