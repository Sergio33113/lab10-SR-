# https://github.com/Sergio33113/lab10-SR-
# Partner 1: Sergio Rivera
# Partner 2: 

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def power(x, y):
    return x ** y

def mod(x, y):
    if y == 0:
        raise ValueError("Cannot mod by zero.")
    return x % y
