from django.test import TestCase
from .models import Deposit


class FDTests(TestCase):
    def test_maturity_math(self):
        d = Deposit(name="A", principal=10000, rate=7, years=2)
        self.assertEqual(d.maturity(), 11449.0)
        self.assertEqual(d.interest(), 1449.0)

    def test_post_saves_and_shows_result(self):
        r = self.client.post('/', {"name": "Asha", "principal": 10000, "rate": 7, "years": 2})
        self.assertContains(r, "11449")
        self.assertEqual(Deposit.objects.count(), 1)

    def test_invalid_post_saves_nothing(self):
        r = self.client.post('/', {"name": "Asha", "principal": -5, "rate": 7, "years": 2})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(Deposit.objects.count(), 0)

    def test_history_lists_saved(self):
        Deposit.objects.create(name="Ravi", principal=5000, rate=6, years=1)
        self.assertContains(self.client.get('/history/'), "Ravi")
