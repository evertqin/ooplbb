#!/usr/bin/env python3

# ------------------
# IntegerSolution.py
# ------------------

from unittest import main, TestCase

""" ----------------------------------------------------------------------
Define integer such that it's an iterable over the digits of the integer
from least to most significant digit.
"""

class UnitTests (TestCase) :
    def setUp (self) :
        self.x = my_integer(234)
        self.p = iter(self.x)

    def test_1 (self) :
        self.assertIs(iter(self.p), self.p)

    def test_2 (self) :
        self.assertEqual(next(self.p), 4)

    def test_3 (self) :
        next(self.p)
        self.assertEqual(next(self.p), 3)

    def test_4 (self) :
        next(self.p)
        next(self.p)
        self.assertEqual(next(self.p), 2)

    def test_5 (self) :
        next(self.p)
        next(self.p)
        next(self.p)
        self.assertRaises(StopIteration, next, self.p)

    def test_6 (self) :
        self.assertEqual(sum(self.x), 9)

    def test_7 (self) :
        self.assertEqual(sum(self.p), 9)

main()
