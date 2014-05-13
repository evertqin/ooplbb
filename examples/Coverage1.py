#!/usr/bin/env python3

# ------------
# Coverage1.py
# ------------

def test (b, c) :
    if b :
        if c :
            print("b is true and c is true")
        else :
            print("b is true and c is false")
    elif c :
        print("b is false and c is true")
    else :
        print("b is false and c is false")

print("Coverage1.py")

test(False, False)

print("Done.")

"""
% coverage help
Coverage.py, version 3.7.1
Measure, collect, and report on code coverage in Python programs.

usage: coverage <command> [options] [args]

Commands:
    annotate    Annotate source files with execution information.
    combine     Combine a number of data files.
    erase       Erase previously collected coverage data.
    help        Get help on using coverage.py.
    html        Create an HTML report.
    report      Report coverage stats on modules.
    run         Run a Python program and measure code execution.
    xml         Create an XML report of coverage results.

Use "coverage help <command>" for detailed help on any command.
Use "coverage help classic" for help on older command syntax.
For more information, see http://nedbatchelder.com/code/coverage



% coverage run --branch Coverage1.py
Coverage1.py
b is false and c is false
Done.

% coverage report
Name        Stmts   Miss Branch BrMiss  Cover
---------------------------------------------
Coverage1      11      4      6      4    53%
"""
