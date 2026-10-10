from django.shortcuts import get_object_or_404, render
from .models import Podcast


def podcast_list(request):
    return render(request, "podcast/list.html", {"podcasts": Podcast.objects.all()})


def podcast_detail(request, id):
    podcast = get_object_or_404(Podcast, id=id)
    return render(request, "podcast/detail.html",
                  {"podcast": podcast, "episodes": podcast.episodes.all()})
