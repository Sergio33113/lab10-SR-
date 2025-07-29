# https://github.com/Sergio33113/lab10-SR-
# Partner 1: Sergio Rivera


import unittest
import calculator
import math

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(100, 10), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(100, 1)

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)

    def test_divide(self):
        self.assertEqual(calculator.div(10, 2), 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-1, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(25), 5)
        with self.assertRaises(ValueError):
            calculator.square_root(-4)

if __name__ == '__main__':
    unittest.main()
