from django.test import TestCase
from .models import Artist


class ArtistTests(TestCase):
    fixtures = ["sample_data"]

    def test_all_main_pages_load(self):
        for url in ['/', '/artist/', '/artist/1/', '/playlist/', '/playlist/1/',
                    '/playlist/liked/', '/podcast/', '/podcast/1/', '/search/']:
            self.assertEqual(self.client.get(url).status_code, 200, url)

    def test_genre_filter(self):
        r = self.client.get('/artist/', {"genre": "Pop"})
        self.assertContains(r, "Taylor Swift")
        self.assertNotContains(r, "Arijit Singh")

    def test_artist_detail_lists_their_songs(self):
        a = Artist.objects.get(name="Arijit Singh")
        r = self.client.get(f'/artist/{a.id}/')
        self.assertContains(r, "Tum Hi Ho")
        self.assertNotContains(r, "Blinding Lights")

    def test_missing_artist_is_404(self):
        self.assertEqual(self.client.get('/artist/9999/').status_code, 404)

    def test_search_finds_song_and_artist(self):
        r = self.client.get('/search/', {"q": "weeknd"})
        self.assertContains(r, "Blinding Lights")
        r = self.client.get('/search/', {"q": "zzzz"})
        self.assertContains(r, "Nothing found")

    def test_followers_use_commas(self):
        self.assertContains(self.client.get('/artist/'), "45,000,000")
