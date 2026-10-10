from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    followers = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["name"]

    def hue(self):
        """A colour number (0-360) used for the round avatar."""
        return (self.id * 47) % 360

    def __str__(self):
        return self.name
