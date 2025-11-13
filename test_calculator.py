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

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(7, 3), 7 / 3)

    ####### Partner 2
    def test_divide_by_zero(self):
        self.assertIsNone(div(0, 5))

    def test_logarithm(self):
        self.assertAlmostEqual(log(8, 2), 3.0)
        self.assertAlmostEqual(log(100, 10), 2.0)
        self.assertAlmostEqual(log(math.e ** 4, math.e), 4.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ZeroDivisionError):
            log(10, 1)

    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(-5, 10)

        with self.assertRaises(ValueError):
            log(10, 1)

        with self.assertRaises(ValueError):
            log(10, -2)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0), 0)

        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()