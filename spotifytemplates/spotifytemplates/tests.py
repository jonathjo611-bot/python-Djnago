import re

from django.conf import settings
from django.test import TestCase
from django.urls import reverse

PAGES = ["home", "artist-detail", "playlist-detail", "podcast-detail"]


class Section1Templates(TestCase):
    # ---- Q1 ----
    def test_q1_home_renders_heading_and_links(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, "home.html")
        self.assertContains(r, "<h1>Welcome to Spotify</h1>", html=True)
        for url in ("/artist/", "/playlist/", "/podcast/"):
            self.assertContains(r, f'href="{url}"')

    def test_q1_every_link_leads_to_a_working_page(self):
        for url in ("/artist/", "/playlist/", "/podcast/"):
            self.assertEqual(self.client.get(url).status_code, 200, url)

    # ---- Q2 ----
    def test_q2_cards_are_divs_wrapped_in_links(self):
        html = self.client.get('/').content.decode()
        cards = re.findall(r'<a class="card-link" href="([^"]+)">\s*<div class="app-card">(\w+)</div>\s*</a>', html)
        self.assertEqual([c[1] for c in cards], ["Artist", "Playlist", "Podcast"])
        self.assertEqual([c[0] for c in cards], ["/artist/", "/playlist/", "/podcast/"])

    def test_q2_cards_use_internal_css_with_border_padding_pointer(self):
        html = self.client.get('/').content.decode()
        self.assertIn("<style>", html)
        block = html[html.index(".app-card {"):].split("}")[0]
        for needed in ("border", "padding", "cursor: pointer"):
            self.assertIn(needed, block)

    # ---- Q3 ----
    def test_q3_project_level_base_is_used_by_every_page(self):
        self.assertIn(settings.BASE_DIR / "templates", settings.TEMPLATES[0]["DIRS"])
        for name in PAGES:
            r = self.client.get(reverse(name))
            self.assertTemplateUsed(r, "base.html", msg_prefix=name)
            for label in ("Home", "Playlists", "Artists", "Podcasts"):
                self.assertContains(r, f">{label}</a>")

    # ---- Q4 ----
    def test_q4_each_app_has_its_own_base_and_colour(self):
        expected = {
            "artist-detail": ("artist/artist.html", "#3b1c5a"),
            "playlist-detail": ("playlist/playlist.html", "#0f5c5c"),
            "podcast-detail": ("podcast/podcast.html", "#7a2e0e"),
        }
        for name, (template, colour) in expected.items():
            r = self.client.get(reverse(name))
            self.assertTemplateUsed(r, template)
            self.assertTemplateUsed(r, "base.html")             # app template extends the project base
            self.assertContains(r, f"background: {colour}")
        self.assertEqual(len({c for _, c in expected.values()}), 3)   # three different colours

    # ---- Q5 ----
    def test_q5_filters_show_correct_output(self):
        r = self.client.get('/artist/')
        self.assertContains(r, "Total artists: <b>3</b>")
        self.assertContains(r, "Luna Ray")                       # |title
        self.assertContains(r, "THE MIDNIGHT BLOOM")             # |upper
        self.assertContains(r, "dj kavi")                        # |lower
        self.assertContains(r, "No bio available")               # |default (empty bio)
        self.assertContains(r, "March 2024")                     # |date:"F Y"
        self.assertContains(r, "4 songs")                        # |length (+ pluralize)
        self.assertContains(r, "Indie pop singer who writes …")  # |truncatewords:5

    # ---- Q6 ----
    def test_q6_all_paths_are_named(self):
        for name in PAGES:
            reverse(name)                                        # raises if a name is missing

    def test_q6_no_hardcoded_links_in_any_template(self):
        offenders = []
        for path in settings.BASE_DIR.rglob("*.html"):
            for line in path.read_text().splitlines():
                if re.search(r'href="/', line) and "{%" not in line:
                    offenders.append(f"{path.name}: {line.strip()}")
        self.assertEqual(offenders, [])

    # ---- Q7 ----
    def test_q7_playlist_has_all_11_songs_with_details(self):
        r = self.client.get('/playlist/')
        self.assertTemplateUsed(r, "playlist/playlist_detail.html")
        self.assertEqual(len(r.context["playlist"]), 11)
        for text in ("BbY WOW", "NO ME ARREPIENTO DE SENTIR TANTO", "33,059,939 plays",
                     "Billie Jean", "Thriller", "Don&#x27;t Forget About Me, Demos"):
            self.assertContains(r, text)

    def test_q7b_now_playing_only_on_first_song(self):
        html = self.client.get('/playlist/').content.decode()
        self.assertEqual(html.count("Now Playing"), 1)
        first_li = html.split('<li class="song">')[1]
        self.assertIn("Now Playing", first_li)
        self.assertIn("BbY WOW", first_li)

    def test_q7c_labels_follow_play_count(self):
        html = self.client.get('/playlist/').content.decode()
        self.assertEqual(html.count("Trending</span>"), 1)       # only BbY WOW (> 25,000,000)
        self.assertEqual(html.count("Popular</span>"), 6)        # > 20,000,000
        self.assertEqual(html.count("Regular</span>"), 4)
        rows = html.split('<li class="song">')[1:]
        self.assertIn("Trending", rows[0])
        self.assertIn("Popular", rows[5])                        # Dai Dai 21,507,155
        self.assertIn("Popular", rows[6])                        # Self Aware 20,891,173
        self.assertIn("Regular", rows[7])                        # the cure 19,826,357

    def test_q7d_empty_state(self):
        r = self.client.get('/playlist/', {"empty": "1"})
        self.assertContains(r, "No songs added yet. Start building your playlist!")
        self.assertNotContains(r, "Now Playing")
        self.assertNotContains(self.client.get('/playlist/'), "No songs added yet")
