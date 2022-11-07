from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):

    def test_add(self):
        res = calc.add(5, 12)

        self.assertEqual(res, 17)

    def test_substract(self):
        res = calc.substract(12, 5)

        self.assertEqual(res, 7)
