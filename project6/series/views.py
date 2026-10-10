from django.shortcuts import render
from .data import SERIES


def series_list(request):
    return render(request, "series/1.html", {"series": SERIES})
