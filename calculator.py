# https://github.com/Sergio33113/lab10-SR-
# Partner 1: Sergio Rivera


import math

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):  
    return x * y

def div(x, y):  
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def mod(x, y):
    if y == 0:
        raise ValueError("Cannot mod by zero.")
    return x % y

def power(x, y):
    return x ** y

def logarithm(x, base=math.e):
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return math.log(x, base)

def exp(x):
    return math.exp(x)

def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of negative number.")
    return math.sqrt(x)

def hypotenuse(a, b):
    return math.hypot(a, b)
