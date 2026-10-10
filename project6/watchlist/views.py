from django.shortcuts import redirect, render
from movies.data import MOVIES


def watchlist(request):
    ids = request.session.get("watchlist", [])
    saved = [m for m in MOVIES if m["id"] in ids]
    return render(request, "watchlist/1.html", {"saved": saved})


def add(request, id):
    if request.method == "POST":
        ids = request.session.get("watchlist", [])
        if id not in ids:
            ids.append(id)
        request.session["watchlist"] = ids
    return redirect("watchlist")


def remove(request, id):
    if request.method == "POST":
        ids = request.session.get("watchlist", [])
        request.session["watchlist"] = [i for i in ids if i != id]
    return redirect("watchlist")
