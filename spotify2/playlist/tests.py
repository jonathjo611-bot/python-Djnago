from django.test import TestCase
from .models import Playlist, Song


class PlaylistTests(TestCase):
    fixtures = ["sample_data"]

    def test_duration_display(self):
        s = Song(title="x", duration=245)
        self.assertEqual(s.duration_display(), "4:05")

    def test_playlist_total_duration(self):
        p = Playlist.objects.get(name="Kannada Classics")   # 245s + 232s = 477s
        self.assertEqual(p.total_duration(), "7 min")

    def test_playlist_detail_shows_songs(self):
        p = Playlist.objects.get(name="Bollywood Hits")
        r = self.client.get(f'/playlist/{p.id}/')
        self.assertContains(r, "Kesariya")
        self.assertNotContains(r, "Shake It Off")

    def test_like_toggle_and_liked_page(self):
        s = Song.objects.get(title="Starboy")
        self.client.post(f'/playlist/like/{s.id}/', {"next": "/"})
        self.assertContains(self.client.get('/playlist/liked/'), "Starboy")
        self.client.post(f'/playlist/like/{s.id}/', {"next": "/"})       # second press un-likes
        self.assertNotContains(self.client.get('/playlist/liked/'), "Starboy")

    def test_like_needs_post(self):
        s = Song.objects.get(title="Starboy")
        self.client.get(f'/playlist/like/{s.id}/')
        self.assertNotContains(self.client.get('/playlist/liked/'), "Starboy")

    def test_like_redirects_back_but_not_to_other_sites(self):
        s = Song.objects.get(title="Starboy")
        r = self.client.post(f'/playlist/like/{s.id}/', {"next": "/artist/"})
        self.assertRedirects(r, '/artist/')
        r = self.client.post(f'/playlist/like/{s.id}/', {"next": "https://evil.example.com/"})
        self.assertRedirects(r, '/playlist/liked/')
