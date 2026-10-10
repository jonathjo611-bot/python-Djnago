from django.test import TestCase
from restaurants.models import MenuItem


def item(name):
    return MenuItem.objects.get(name=name)


class CartTests(TestCase):
    fixtures = ["sample_data"]

    def add(self, name, **extra):
        return self.client.post(f'/cart/add/{item(name).id}/', extra)

    def test_add_item_and_bill(self):
        # Dosa Darbar: delivery Rs 20. Masala Dosa Rs 99 x 2 = 198, GST 5% = 10 (9.9 rounded)
        self.add("Masala Dosa")
        self.add("Masala Dosa")
        cart = self.client.get('/cart/').context["cart"]
        self.assertEqual(cart["count"], 2)
        self.assertEqual(cart["subtotal"], 198)
        self.assertEqual(cart["delivery_fee"], 20)
        self.assertEqual(cart["tax"], 10)
        self.assertEqual(cart["total"], 228)

    def test_navbar_badge_counts_items(self):
        self.add("Masala Dosa")
        self.add("Filter Coffee")
        self.assertEqual(self.client.get('/').context["cart_count"], 2)

    def test_stepper_increase_decrease_remove(self):
        self.add("Masala Dosa")
        i = item("Masala Dosa").id
        self.client.post(f'/cart/update/{i}/', {"action": "inc"})
        self.assertEqual(self.client.get('/cart/').context["cart"]["count"], 2)
        self.client.post(f'/cart/update/{i}/', {"action": "dec"})
        self.client.post(f'/cart/update/{i}/', {"action": "dec"})
        self.assertEqual(self.client.get('/cart/').context["cart"]["count"], 0)

    def test_other_restaurant_asks_before_replacing(self):
        self.add("Masala Dosa")
        r = self.add("Margherita")                       # different restaurant
        self.assertContains(r, "Replace cart items?")
        self.assertEqual(self.client.get('/cart/').context["cart"]["restaurant"].name, "Dosa Darbar")
        self.add("Margherita", replace="1")
        cart = self.client.get('/cart/').context["cart"]
        self.assertEqual(cart["restaurant"].name, "Pizza Piazza")
        self.assertEqual(cart["count"], 1)

    def test_free_delivery_restaurant(self):
        self.add("Jalebi (250 g)")                       # Sweet Tooth Mithai has free delivery
        self.assertEqual(self.client.get('/cart/').context["cart"]["delivery_fee"], 0)

    def test_below_minimum_is_flagged(self):
        self.add("Filter Coffee")                        # Rs 39, minimum is Rs 99
        r = self.client.get('/cart/')
        self.assertTrue(r.context["below_min"])
        self.assertEqual(r.context["short_by"], 60)

    def test_add_needs_post(self):
        self.client.get(f'/cart/add/{item("Masala Dosa").id}/')
        self.assertEqual(self.client.get('/cart/').context["cart"]["count"], 0)

    def test_next_redirect_cannot_leave_site(self):
        r = self.add("Masala Dosa", next="https://evil.example.com/")
        self.assertNotIn("evil", r["Location"])

    def test_clear_cart(self):
        self.add("Masala Dosa")
        self.client.post('/cart/clear/')
        self.assertEqual(self.client.get('/cart/').context["cart"]["count"], 0)
