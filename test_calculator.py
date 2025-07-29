# https://github.com/Sergio33113/lab10-SR-
# Partner 1: Sergio Rivera

import unittest
import calculator
import math

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)

    def test_mul(self):
        self.assertEqual(calculator.mul(4, 3), 12)

    def test_div(self):
        self.assertEqual(calculator.div(10, 2), 5)
        with self.assertRaises(ValueError):
            calculator.div(5, 0)

    def test_mod(self):
        self.assertEqual(calculator.mod(10, 3), 1)
        with self.assertRaises(ValueError):
            calculator.mod(10, 0)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(math.e), 1, places=5)
        self.assertAlmostEqual(calculator.logarithm(100, 10), 2)
        with self.assertRaises(ValueError):
            calculator.logarithm(-1)

    def test_exp(self):
        self.assertAlmostEqual(calculator.exp(1), math.e, places=5)

    def test_square_root(self):
        self.assertEqual(calculator.square_root(25), 5)
        with self.assertRaises(ValueError):
            calculator.square_root(-4)

    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(3, 4), 5)

if __name__ == '__main__':
    unittest.main()

