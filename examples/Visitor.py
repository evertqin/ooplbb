#!/usr/bin/env python3

# ----------
# Visitor.py
# ----------

# http://en.wikipedia.org/wiki/Visitor_pattern

class List :
    def __len__ (self) :
        return self.accept(LengthVisitor())

class Nil (List) :
    def accept (self, v) :
        return v.visit_nil(self)

class Cons (List) :
    def __init__ (self, first, rest) :
        self.__first = first
        self.__rest  = rest

    def accept (self, v) :
        return v.visit_cons(self)

    def first (self) :
        return self.__first

    def rest (self) :
        return self.__rest

class LengthVisitor :
    def visit_nil (self, x) :
        return 0

    def visit_cons (self, x) :
        return len(x.rest()) + 1

print("Visitor.py")

x    = Nil()
x4   = Cons(4, x)
x34  = Cons(3, x4)
x234 = Cons(2, x34)

assert len(   x) == 0
assert len(  x4) == 1
assert len( x34) == 2
assert len(x234) == 3

print("Done.")
