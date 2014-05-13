#!/usr/bin/env python3

# ------------
# UnitTests.py
# ------------

import unittest

class UnitTests (unittest.TestCase) :
    def test_1 (self) :
        self.assertTrue(1 == 2)

    def test_2 (self) :
        self.assertTrue(2 == 2)

    def test_3 (self) :
        self.assertTrue(3 == 2)

unittest.main()

"""
F.F
======================================================================
FAIL: test_1 (__main__.UnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests.py", line 11, in test_1
    self.assertTrue(1 == 2)
assert ionError: False is not true

======================================================================
FAIL: test_3 (__main__.UnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests.py", line 17, in test_3
    self.assertTrue(3 == 2)
assert ionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=2)
"""
