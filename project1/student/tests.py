from django.test import TestCase


class ProfileCardTest(TestCase):
    def test_page_shows_student_details(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jonath Kumar")
        self.assertContains(response, "KU2027-001")
        self.assertContains(response, "<li>Python</li>", html=True)
