#!/usr/bin/env python

# ----------
# Visitor.py
# ----------

# http://en.wikipedia.org/wiki/Visitor_pattern

""" ----------------------------------------------------------------------
Define:
	Nil
	Cons
	LengthVisitor
"""

from unittest import main, TestCase

class UnitTests (TestCase) :
    def setUp (self) :
        self.x    = Nil()
        self.x4   = Cons(4, self.x)
        self.x34  = Cons(3, self.x4)
        self.x234 = Cons(2, self.x34)

    def test_1 (self) :
        self.assertEqual(len(self.x), 0)

    def test_2 (self) :
        self.assertEqual(len(self.x4), 1)

    def test_3 (self) :
        self.assertEqual(len(self.x34), 2)

    def test_4 (self) :
        self.assertEqual(len(self.x234), 3)

main()
