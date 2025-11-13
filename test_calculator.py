# https://github.com/Alex1Hart/lab11-AH-DO
# Partner 1: Alexander Hart
# Partner 2: Diego Ortiz

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):  # 3 assertions
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(10, -2), 8)
        self.assertEqual(add(-5, -5), -10)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, -3), 8)
        self.assertEqual(subtract(-5, 5), -10)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)

        self.assertEqual(mul(5, 0), 0)
    def test_divide(self):  # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(3, 7), 7 / 3)
        self.assertEqual(div(5, 0), 0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(8, 2), 3.0)
        self.assertAlmostEqual(logarithm(100, 10), 2.0)
        self.assertAlmostEqual(logarithm(math.e ** 4, math.e), 4.0)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            logarithm(10, 1)

    def test_divide_by_zero(self):
        # Assumes your divide function catches the error and returns None
        self.assertIsNone(div(0, 5))

    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-5, 10)
        with self.assertRaises(ValueError):
            logarithm(10, -2)

    ####### Partner 1

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)

        self.assertAlmostEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0), 0)

        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()