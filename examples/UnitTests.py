#!/usr/bin/env python3

# ------------
# UnitTests.py
# ------------

from unittest import main, TestCase

def cycle_length (n) :
    assert n > 0
    c = 0
    while n > 1 :
        if (n % 2) == 0 :
            n = (n / 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class UnitTests (TestCase) :
    def test_1 (self) :
        self.assertTrue(cycle_length( 1) == 1)

    def test_2 (self) :
        self.assertTrue(cycle_length( 5) == 6)

    def test_3 (self) :
        self.assertTrue(cycle_length(10) == 7)

main()

"""
FFF
======================================================================
FAIL: test_1 (__main__.UnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests.py", line 23, in test_1
    self.assertTrue(cycle_length( 1) == 1)
  File "./UnitTests.py", line 18, in cycle_length
    assert c > 0
AssertionError

======================================================================
FAIL: test_2 (__main__.UnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests.py", line 26, in test_2
    self.assertTrue(cycle_length( 5) == 6)
AssertionError: False is not true

======================================================================
FAIL: test_3 (__main__.UnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests.py", line 29, in test_3
    self.assertTrue(cycle_length(10) == 7)
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=3)
"""
