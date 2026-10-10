from django.test import TestCase
from .views import calculate_bill


class BillTests(TestCase):
    def test_slab_math(self):
        # 250 units = 100*3 + 100*5 + 50*7 = 300 + 500 + 350 = 1150
        breakdown, energy = calculate_bill(250)
        self.assertEqual(energy, 1150)
        self.assertEqual(len(breakdown), 3)

    def test_zero_units(self):
        self.assertEqual(calculate_bill(0)[1], 0)

    def test_form_page_loads(self):
        self.assertEqual(self.client.get('/').status_code, 200)

    def test_post_shows_total(self):
        r = self.client.post('/', {"name": "Asha", "units": 250})
        self.assertContains(r, "Rs 1200")  # 1150 + 50 fixed

    def test_invalid_post_shows_form_again(self):
        r = self.client.post('/', {"name": "Asha", "units": -5})
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "Calculate")
