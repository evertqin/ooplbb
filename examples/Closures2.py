#!/usr/bin/env python3

# ------------
# Closures2.py
# ------------

from functools import reduce
from operator  import add
from unittest  import TestCase, TestLoader, TestSuite, TextTestRunner

def sum_for (a) :
    s = 0
    for w in a :
        s += w
    return s

def sum_reduce (a) :
    return reduce(add, a, 0)

def bind (my_sum) :
	class UnitTests (TestCase) :
		def test_1 (self) :
			self.assertTrue(my_sum([]) == 0)

		def test_2 (self) :
			self.assertTrue(my_sum([2]) == 2)

		def test_3 (self) :
			self.assertTrue(my_sum([2, 3]) == 5)

		def test_4 (self) :
			self.assertTrue(my_sum([2, 3, 4]) == 9)
	return UnitTests

s = TestSuite()
s.addTest(TestLoader().loadTestsFromTestCase(bind(sum_for)))
s.addTest(TestLoader().loadTestsFromTestCase(bind(sum_reduce)))
TextTestRunner().run(s)
