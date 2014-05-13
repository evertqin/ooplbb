#!/usr/bin/env python3

# -------------
# Assertions.py
# -------------

"""
Turn OFF assert ions at run time with -O.
% python -O assertions.py
"""

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

print("assert ions.py")

assert cycle_length(1) == 1
assert cycle_length(5) == 6

print("Done.")

"""
assert ions.py
Traceback (most recent call last):
  File "./assert ions.py", line 26, in <module>
    assert cycle_length(1) == 1
  File "./assert ions.py", line 23, in cycle_length
    assert c > 0
assert ionError
"""
