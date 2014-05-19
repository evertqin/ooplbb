#!/usr/bin/env python3

# -----------
# Collatz1.py
# -----------

# http://www.spoj.com/problems/PROBTNPO/

"""
% Collatz1.py
1 10
1 10 20
100 200
100 200 125
201 210
201 210

% Collatz1.py < Collatz.in > Collatz.tmp

% diff Collatz.tmp Collatz.out
"""

""" ----------------------------------------------------------------------
Define:
    collatz_read()
    collatz_eval()
    collatz_print()
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
