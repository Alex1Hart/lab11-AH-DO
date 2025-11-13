# https://github.com/Alex1Hart/lab11-AH-DO
# Partner 1: Alexander Hart
# Partner 2: Diego Ortiz



"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math
# First example
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return b / a
    except ZeroDivisionError:
        print("Error")

def logarithm(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        raise ValueError("Invalid input.")

def exponent(a, b): return a**b


def square_root(a):

    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)


