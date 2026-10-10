from django.shortcuts import get_object_or_404, render
from .models import Artist


def artist_list(request):
    genre = request.GET.get("genre", "")
    artists = Artist.objects.all()
    if genre:
        artists = artists.filter(genre=genre)
    genres = Artist.objects.order_by("genre").values_list("genre", flat=True).distinct()
    return render(request, "artist/list.html",
                  {"artists": artists, "genres": genres, "current": genre})


def artist_detail(request, id):
    artist = get_object_or_404(Artist, id=id)
    context = {
        "artist": artist,
        "songs": artist.songs.all(),
        "liked": request.session.get("liked", []),
    }
    return render(request, "artist/detail.html", context)
