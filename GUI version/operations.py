# add, subtract, multiply, divide
import math
def add(a, b):
    return a+b 

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: Division by zero"
    
#Advanced operations
def squareroot(a):
    if a < 0:
        return "Error : Negative Number!."
    return math.sqrt(a)

def factorial(a):
    if a <0:
        return "Error : Negative Number!."
    return math.factorial(a)

def sine(a):
    return math.sin(math.radians(a))
def cosine(a):
    return math.cos(math.radians(a))
def tangent(a):
    return math.tan(math.radians(a))