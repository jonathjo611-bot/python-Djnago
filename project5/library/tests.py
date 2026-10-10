from django.test import TestCase


class LibraryTests(TestCase):
    fixtures = ["books"]

    def test_list_shows_all_books(self):
        r = self.client.get('/')
        self.assertContains(r, "Wings of Fire")
        self.assertContains(r, "Organic Chemistry")

    def test_search_by_author(self):
        r = self.client.get('/', {"q": "narayan"})
        self.assertContains(r, "The Guide")
        self.assertContains(r, "Malgudi Days")
        self.assertNotContains(r, "Wings of Fire")

    def test_detail_page(self):
        self.assertContains(self.client.get('/book/4/'), "Stephen Hawking")

    def test_missing_book_is_404(self):
        self.assertEqual(self.client.get('/book/999/').status_code, 404)
