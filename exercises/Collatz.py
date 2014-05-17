#!/usr/bin/env python3

# ----------
# Collatz.py
# ----------

# http://www.spoj.com/problems/PROBTNPO/

""" ----------------------------------------------------------------------
Define:
	collatz_read
	collatz_eval
	collatz_print
"""

from sys import stdin, stdout

def collatz_solve (r, w) :
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)

if __name__ == '__main__' :
    collatz_solve(stdin, stdout)
