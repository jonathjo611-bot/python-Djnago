from django.db import models


class Podcast(models.Model):
    title = models.CharField(max_length=150)
    host = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def hue(self):
        return (self.id * 61) % 360

    def __str__(self):
        return self.title


class Episode(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name="episodes")
    title = models.CharField(max_length=200)
    minutes = models.PositiveIntegerField()
    released = models.DateField()

    class Meta:
        ordering = ["-released"]

    def __str__(self):
        return self.title
