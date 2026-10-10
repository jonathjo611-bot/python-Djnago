from django.test import TestCase
from .models import Student


def make(**kw):
    data = dict(name="Asha", roll_no="R1", maths=90, science=90, english=90)
    data.update(kw)
    return Student.objects.create(**data)


class MarksTests(TestCase):
    def test_grade_boundaries(self):
        self.assertEqual(make(roll_no="a").grade(), "A+")
        self.assertEqual(make(roll_no="b", maths=80, science=80, english=80).grade(), "A")
        self.assertEqual(make(roll_no="c", maths=30, science=30, english=30).grade(), "F")

    def test_add_redirects_to_list(self):
        r = self.client.post('/', {"name": "Ravi", "roll_no": "R9", "maths": 70, "science": 60, "english": 80})
        self.assertRedirects(r, '/list/')
        self.assertEqual(Student.objects.count(), 1)

    def test_marks_over_100_rejected(self):
        self.client.post('/', {"name": "X", "roll_no": "R2", "maths": 101, "science": 60, "english": 80})
        self.assertEqual(Student.objects.count(), 0)

    def test_list_shows_class_average(self):
        make(roll_no="a")
        self.assertContains(self.client.get('/list/'), "90.0")

    def test_delete_needs_post(self):
        s = make()
        self.client.get(f'/delete/{s.id}/')
        self.assertEqual(Student.objects.count(), 1)
        self.client.post(f'/delete/{s.id}/')
        self.assertEqual(Student.objects.count(), 0)
