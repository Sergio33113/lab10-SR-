# https://github.com/Sergio33113/lab10-SR-
# Partner 1: Sergio Rivera
# Partner 2: 

import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            calculator.divide(5, 0)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)

    def test_mod(self):
        self.assertEqual(calculator.mod(10, 3), 1)
        with self.assertRaises(ValueError):
            calculator.mod(10, 0)

if __name__ == '__main__':
    unittest.main()
