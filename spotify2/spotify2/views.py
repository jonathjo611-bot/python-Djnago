from django.db.models import Q
from django.shortcuts import render

from artist.models import Artist
from playlist.models import Playlist, Song
from podcast.models import Podcast


def home(request):
    context = {
        "artists": Artist.objects.order_by("-followers")[:6],
        "songs": Song.objects.select_related("artist")[:5],      # already ordered by plays
        "playlists": Playlist.objects.all()[:4],
        "podcasts": Podcast.objects.all()[:3],
        "liked": request.session.get("liked", []),
    }
    return render(request, "home.html", context)


def search(request):
    q = request.GET.get("q", "").strip()
    artists = songs = podcasts = []
    if q:
        artists = Artist.objects.filter(Q(name__icontains=q) | Q(genre__icontains=q))
        songs = Song.objects.filter(
            Q(title__icontains=q) | Q(album__icontains=q) | Q(artist__name__icontains=q)
        ).select_related("artist")
        podcasts = Podcast.objects.filter(Q(title__icontains=q) | Q(host__icontains=q))
    context = {
        "q": q, "artists": artists, "songs": songs, "podcasts": podcasts,
        "liked": request.session.get("liked", []),
        "found": bool(artists or songs or podcasts),
    }
    return render(request, "search.html", context)
