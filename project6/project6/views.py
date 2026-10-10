from django.shortcuts import render
from movies.data import MOVIES
from series.data import SERIES


def home(request):
    context = {"movies": MOVIES[:3], "series": SERIES[:3]}
    return render(request, "home.html", context)
