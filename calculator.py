"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math
# First example
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return b / a
    except ZeroDivisionError:
        print("Error")

def log(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        raise ValueError("Invalid input.")

def exp(a, b): return a**b


import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):

    return math.log(b, a)

def exponent(a, b):
    return a ** b
