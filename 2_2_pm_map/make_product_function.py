"""Coding exercise


Python has built-in sum, but no product. Write a product function

Spec: mimic `np.product`, aka RYO (roll your own)
"""

# Tests:

import numpy as np

items = ([1, 3, 2],
         (42, 42, 42),
         np.linspace(0, 10),
         range(10))
 
for item in items:
    assert product(item) == np.product(item)

# Functional

from functools import reduce 
import operator as op

def product(iterable):
    "Like the sum built-in but for multiplication, similar to numpy.product"
    return reduce(lambda x,y: x*y, iterable)

def product(iterable):
    "Like the sum built-in but for multiplication, similar to numpy.product"
    return reduce(op.mul, iterable)

# Abstraction
def apply(iterable=None, operator=op.mul):
    "Like the sum built-in but for multiplication, similar to numpy.product"
    return reduce(operator, iterable)

# Complex example
apply(range(1, 10),
         operator = lambda x,y: (x+10)**2)

def apply(iterable=None, operator=op.mul):
    "Like the sum built-in but for multiplication, similar to numpy.product"
    return reduce(operator, iterable)