from django.db import models
from artist.models import Artist


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")
    album = models.CharField(max_length=200)
    plays = models.PositiveBigIntegerField(default=0)
    duration = models.PositiveIntegerField(help_text="Length in seconds")

    class Meta:
        ordering = ["-plays"]

    def duration_display(self):
        minutes, seconds = divmod(self.duration, 60)
        return f"{minutes}:{seconds:02d}"

    def __str__(self):
        return f"{self.title} - {self.artist}"


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    songs = models.ManyToManyField(Song, blank=True, related_name="playlists")

    def hue(self):
        return (self.id * 83) % 360

    def total_duration(self):
        total = sum(s.duration for s in self.songs.all())
        minutes = total // 60
        if minutes >= 60:
            return f"{minutes // 60} hr {minutes % 60} min"
        return f"{minutes} min"

    def __str__(self):
        return self.name
