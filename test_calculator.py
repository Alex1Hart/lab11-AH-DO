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
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

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
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
    #
    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    # #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()