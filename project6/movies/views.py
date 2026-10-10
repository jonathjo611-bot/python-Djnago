from django.http import Http404
from django.shortcuts import render
from .data import MOVIES


def movie_list(request):
    return render(request, "movies/1.html", {"movies": MOVIES})


def movie_detail(request, id):
    movie = next((m for m in MOVIES if m["id"] == id), None)
    if movie is None:
        raise Http404("No such movie")
    saved = id in request.session.get("watchlist", [])
    return render(request, "movies/2.html", {"movie": movie, "saved": saved})
