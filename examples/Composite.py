#!/usr/bin/env python3

# ------------
# Composite.py
# ------------

# http://en.wikipedia.org/wiki/Composite_pattern

class Nil () :
    def __len__ (self) :
        return 0

class Cons () :
    def __init__ (self, first, rest) :
        self.__first = first
        self.__rest  = rest

    def __len__ (self) :
        return len(self.rest()) + 1

    def first (self) :
        return self.__first

    def rest (self) :
        return self.__rest

print('Composite.py')

x    = Nil()
x4   = Cons(4, x)
x34  = Cons(3, x4)
x234 = Cons(2, x34)

assert len(   x) == 0
assert len(  x4) == 1
assert len( x34) == 2
assert len(x234) == 3

print("Done.")
