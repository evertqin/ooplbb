#!/usr/bin/env python3

# ----------
# Binders.py
# ----------

from operator import sub

print("Binders.py")

def bind1st (bf, x) :
    return lambda y : bf(x, y)

def bind2nd (bf, y) :
    return lambda x : bf(x, y)

assert bind1st(sub, 2)(3) == -1
assert bind2nd(sub, 2)(3) ==  1

print("Done.")
