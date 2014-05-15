#!/usr/bin/env python3

# ------------
# Coverage2.py
# ------------

from unittest import main, TestCase

def cycle_length (n) :
    assert n > 0
    c = 1
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
        self.assertEqual(cycle_length( 1), 1)

    def test_2 (self) :
        self.assertEqual(cycle_length( 2), 2)

main()

"""
% coverage run --branch Coverage2.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK



% coverage report -m
Name        Stmts   Miss Branch BrMiss  Cover   Missing
-------------------------------------------------------
Coverage2      18      2      4      1    86%   16, 30
"""
