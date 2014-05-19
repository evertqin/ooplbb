#!/usr/bin/env python3

""" ----------------------------------------------------------------------
What is the output of the following?
"""

class A :
    def f1 (self) :
        return self.f2()

    def f2 (self) :
        return "A.f2"

    def g1 (self) :
        return self.g2()

    @staticmethod
    def g2 () :
        return "A.g2"

    def h1 (self) :
        return self.__h2()

    def __h2 (self) :
        return "A.h2"

class B (A) :
    def f2 (self) :
        return "B.f2"

    @staticmethod
    def g2 () :
        return "B.g2"

    def __h2 (self) :
        return "B.h2"

print("DynamicBinding.py")

x = A()
print(x.f1())
print(x.g1())
print(x.h1())
print()

x = B()
print(x.f1())
print(x.g1())
print(x.h1())

print("Done.")
