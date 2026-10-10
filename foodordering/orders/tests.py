from django.test import Client, TestCase
from restaurants.models import MenuItem
from .models import Order

GOOD = {"name": "Asha", "phone": "9876543210", "address": "12 Lake Road", "payment": "cod"}


class OrderTests(TestCase):
    fixtures = ["sample_data"]

    def fill_cart(self, client=None, name="Masala Dosa", times=2):
        c = client or self.client
        for _ in range(times):
            c.post(f'/cart/add/{MenuItem.objects.get(name=name).id}/')

    def test_empty_cart_cannot_checkout(self):
        self.assertRedirects(self.client.get('/checkout/'), '/cart/')

    def test_place_order_saves_everything_and_clears_cart(self):
        self.fill_cart()
        r = self.client.post('/checkout/', GOOD)
        order = Order.objects.get()
        self.assertRedirects(r, f'/orders/{order.id}/')
        self.assertEqual((order.subtotal, order.delivery_fee, order.tax, order.total), (198, 20, 10, 228))
        self.assertEqual(order.items.get().quantity, 2)
        self.assertEqual(order.status, "placed")
        self.assertEqual(self.client.get('/cart/').context["cart"]["count"], 0)

    def test_bad_phone_is_rejected(self):
        self.fill_cart()
        r = self.client.post('/checkout/', dict(GOOD, phone="12345"))
        self.assertContains(r, "valid 10-digit")
        self.assertEqual(Order.objects.count(), 0)

    def test_below_minimum_blocks_order(self):
        self.fill_cart(name="Filter Coffee", times=1)
        self.client.post('/checkout/', GOOD)
        self.assertEqual(Order.objects.count(), 0)

    def test_order_keeps_price_after_menu_changes(self):
        self.fill_cart()
        self.client.post('/checkout/', GOOD)
        MenuItem.objects.filter(name="Masala Dosa").update(price=500)
        self.assertEqual(Order.objects.get().items.get().price, 99)

    def test_history_and_tracking_only_for_my_orders(self):
        self.fill_cart()
        self.client.post('/checkout/', GOOD)
        order = Order.objects.get()
        self.assertContains(self.client.get('/orders/'), "Dosa Darbar")
        self.assertEqual(self.client.get(f'/orders/{order.id}/').status_code, 200)
        stranger = Client()
        self.assertEqual(stranger.get(f'/orders/{order.id}/').status_code, 404)
        self.assertNotContains(stranger.get('/orders/'), "Dosa Darbar")

    def test_demo_advance_walks_through_statuses(self):
        self.fill_cart()
        self.client.post('/checkout/', GOOD)
        order = Order.objects.get()
        seen = [order.status]
        for _ in range(4):
            self.client.post(f'/orders/{order.id}/advance/')
            order.refresh_from_db()
            seen.append(order.status)
        self.assertEqual(seen, ["placed", "preparing", "on_the_way", "delivered", "delivered"])

    def test_stranger_cannot_advance_my_order(self):
        self.fill_cart()
        self.client.post('/checkout/', GOOD)
        order = Order.objects.get()
        Client().post(f'/orders/{order.id}/advance/')
        order.refresh_from_db()
        self.assertEqual(order.status, "placed")
