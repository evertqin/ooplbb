#!/usr/bin/env python3

# --------
# Range.py
# --------

import sys
import time

class range_iterator () :
    def __init__ (self, b, e) :
        self.b = b
        self.e = e

    def __iter__ (self) :
        return self

    def __next__ (self) :
        if self.b == self.e :
            raise StopIteration()
        p = self.b
        self.b += 1
        return p

def range_generator (b, e) :
    while b != e :
        yield b
        b += 1

def test (f) :
    print(f.__name__)
    assert list(f(2, 2)) == []
    assert list(f(2, 3)) == [2]
    assert list(f(2, 4)) == [2, 3]
    assert list(f(2, 5)) == [2, 3, 4]
    b = time.clock()
    sum(f(1, 100))
    e = time.clock()
    print("%5.3f" % ((e - b) * 1000), "milliseconds")
    print()

print("Range.py")
print()

print(sys.version)
print()

test(range_iterator)
test(range_generator)
test(range)

print("Done.")

"""
Range.py

3.3.3 (default, Jan 19 2014, 09:53:07)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.2.79)]

range_iterator
0.134 milliseconds

range_generator
0.029 milliseconds

range
0.006 milliseconds

Done.
"""
