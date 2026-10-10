from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from .models import Playlist, Song


def playlist_list(request):
    return render(request, "playlist/list.html", {"playlists": Playlist.objects.all()})


def playlist_detail(request, id):
    playlist = get_object_or_404(Playlist, id=id)
    context = {
        "playlist": playlist,
        "songs": playlist.songs.select_related("artist"),
        "liked": request.session.get("liked", []),
    }
    return render(request, "playlist/detail.html", context)


def liked_songs(request):
    ids = request.session.get("liked", [])
    songs = Song.objects.filter(id__in=ids).select_related("artist")
    return render(request, "playlist/liked.html", {"songs": songs, "liked": ids})


def like(request, id):
    """Heart / un-heart a song. The liked ids are remembered in the session."""
    get_object_or_404(Song, id=id)
    if request.method == "POST":
        ids = request.session.get("liked", [])
        if id in ids:
            ids.remove(id)
        else:
            ids.append(id)
        request.session["liked"] = ids

    # go back to the page the user came from, but only if it is on this site
    next_url = request.POST.get("next", "")
    if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        next_url = reverse("liked")
    return redirect(next_url)
