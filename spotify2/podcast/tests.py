from django.test import TestCase
from .models import Podcast


class PodcastTests(TestCase):
    fixtures = ["sample_data"]

    def test_list_shows_episode_counts(self):
        self.assertContains(self.client.get('/podcast/'), "3 episodes")

    def test_detail_shows_episodes_newest_first(self):
        p = Podcast.objects.get(title="Code & Chai")
        r = self.client.get(f'/podcast/{p.id}/')
        text = r.content.decode()
        self.assertLess(text.index("Debugging without panic"), text.index("Models, forms and views explained"))
        self.assertContains(r, "3 Oct 2026")

    def test_missing_podcast_is_404(self):
        self.assertEqual(self.client.get('/podcast/9999/').status_code, 404)
