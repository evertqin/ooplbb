#!/usr/bin/env python3

# ----------
# IsPrime.py
# ----------

""" ----------------------------------------------------------------------
There's a bug in the tests.
There's a bug in the code.
Find them, fix them, and improve the coverage
"""

from math     import sqrt
from unittest import main, TestCase

def is_prime (n) :
    assert n > 0
    if (n < 2) or ((n % 2) == 0) :
        return False
    for i in range(3, int(sqrt(n))) :
        if (n % i) == 0:
            return False
    return True

class UnitTests (TestCase) :
    def test_1 (self) :
        self.assertFalse(is_prime(1))

    def test_2 (self) :
        self.assertFalse(is_prime(2))

    def test_3 (self) :
        self.assertTrue(is_prime(3))

    def test_4 (self) :
        self.assertFalse(is_prime(4))

    def test_5 (self) :
        self.assertTrue(is_prime(5))

main()

"""
% coverage run --branch IsPrime.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK

% coverage report -m
Name      Stmts   Miss Branch BrMiss  Cover   Missing
-----------------------------------------------------
IsPrime      24      3      6      3    80%   17-18, 39
"""
