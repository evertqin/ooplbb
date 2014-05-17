#!/usr/bin/env python3

# -------
# Copy.py
# -------

from copy import copy, deepcopy

print("Copy.py")

class A :
    def __init__ (self) :
        self.a = [2, 3, 4]

x = A()
y = copy(x)
assert x   is not y
assert x.a is     y.a

y = deepcopy(x)
assert x   is not y
assert x.a is not y.a
assert x.a ==     y.a

print("Done.")
