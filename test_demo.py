import unittest
from demo import Calculator

class TestCalculator(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(Calculator("suma",5,7).suma(), 12)
    def test_rest(self):
        self.assertEqual(Calculator("resta",12,7).resta(), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
   