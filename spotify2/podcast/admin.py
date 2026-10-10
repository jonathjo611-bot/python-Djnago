from django.contrib import admin
from .models import Episode, Podcast


class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ("title", "host", "category")
    inlines = [EpisodeInline]
