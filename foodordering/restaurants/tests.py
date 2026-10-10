from django.test import TestCase
from .models import MenuItem, Restaurant


class RestaurantTests(TestCase):
    fixtures = ["sample_data"]

    def test_list_shows_all_restaurants(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.context["restaurants"]), 9)
        for name in ["Biryani Bazaar", "Dosa Darbar", "Pizza Piazza", "Wok This Way", "Burger Barn",
                     "Kebab Kingdom", "Sweet Tooth Mithai", "Veggie Vibes", "Chettinad Chronicles"]:
            self.assertContains(r, name)

    def test_search_finds_restaurant_by_dish(self):
        r = self.client.get('/', {"q": "ghee roast"})
        self.assertContains(r, "Dosa Darbar")
        self.assertNotContains(r, "Pizza Piazza")

    def test_cuisine_filter(self):
        r = self.client.get('/', {"cuisine": "South Indian"})
        names = [x.name for x in r.context["restaurants"]]
        self.assertCountEqual(names, ["Dosa Darbar", "Chettinad Chronicles"])

    def test_pure_veg_filter(self):
        r = self.client.get('/', {"veg": "1"})
        self.assertTrue(all(x.pure_veg for x in r.context["restaurants"]))
        self.assertEqual(len(r.context["restaurants"]), 3)

    def test_sort_by_fastest(self):
        r = self.client.get('/', {"sort": "time"})
        times = [x.delivery_minutes for x in r.context["restaurants"]]
        self.assertEqual(times, sorted(times))

    def test_pure_veg_restaurants_have_no_nonveg_items(self):
        for rest in Restaurant.objects.filter(pure_veg=True):
            self.assertFalse(rest.menu.filter(veg=False).exists(), rest.name)

    def test_detail_groups_menu_by_section(self):
        rest = Restaurant.objects.get(name="Dosa Darbar")
        r = self.client.get(f'/restaurant/{rest.id}/')
        self.assertContains(r, "Masala Dosa")
        text = r.content.decode()
        self.assertLess(text.index("Tiffin"), text.index("Dosas"))   # sections follow section_order

    def test_missing_restaurant_404(self):
        self.assertEqual(self.client.get('/restaurant/9999/').status_code, 404)
