from django.test import TestCase


class SiteTests(TestCase):
    def test_all_pages_load(self):
        for url in ['/', '/movies/', '/movies/1/', '/series/', '/watchlist/']:
            self.assertEqual(self.client.get(url).status_code, 200, url)

    def test_pages_use_base_template(self):
        self.assertContains(self.client.get('/series/'), "CineBox")
        self.assertContains(self.client.get('/series/'), "css/style.css")

    def test_missing_movie_is_404(self):
        self.assertEqual(self.client.get('/movies/99/').status_code, 404)

    def test_watchlist_add_and_remove(self):
        self.client.post('/watchlist/add/2/')
        self.assertContains(self.client.get('/watchlist/'), "3 Idiots")
        self.assertContains(self.client.get('/movies/2/'), "Already in your watchlist")
        self.client.post('/watchlist/remove/2/')
        self.assertNotContains(self.client.get('/watchlist/'), "3 Idiots")
