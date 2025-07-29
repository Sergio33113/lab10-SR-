# https://github.com/Sergio33113/lab10-SR-
# Partner 1: Sergio Rivera
# Partner 2: Sergio Rivera

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def log(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid input for logarithm.")
    return math.log(a, b)

def exp(a, b):
    return a ** b

def run_unit_tests():
    import unittest
    from test_calculator import TestCalculator

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    result = unittest.TextTestRunner().run(suite)
    return result.wasSuccessful()

run_unit_tests()
