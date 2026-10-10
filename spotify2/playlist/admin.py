from django.contrib import admin
from .models import Playlist, Song


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "album", "plays", "duration")
    list_filter = ("artist",)
    search_fields = ("title", "album", "artist__name")


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    filter_horizontal = ("songs",)
