#!/usr/bin/env python3

# ------------
# Decorator.py
# ------------

# http://en.wikipedia.org/wiki/Decorator_pattern

""" ----------------------------------------------------------------------
Define:
	Pizza
	PizzaDecorator
	CheesePizzaDecorator
	SausagePizzaDecorator
"""

from unittest import main, TestCase

class UnitTests (TestCase) :
    def test_1 (self) :
        p = Pizza()
        self.assertEqual(p.cost(), 7)
        self.assertEqual(str(p), "Pizza")

    def test_2 (self) :
        p = CheesePizzaDecorator(Pizza())
        self.assertEqual(p.cost(), 8)
        self.assertEqual(str(p), "Cheese Pizza")

    def test_3 (self) :
        p = SausagePizzaDecorator(CheesePizzaDecorator(Pizza()))
        self.assertEqual(p.cost(), 10)
        self.assertEqual(str(p), "Sausage Cheese Pizza")

    def test_4 (self) :
        p = CheesePizzaDecorator(SausagePizzaDecorator(CheesePizzaDecorator(Pizza())))
        self.assertEqual(p.cost(), 11)
        self.assertEqual(str(p), "Cheese Sausage Cheese Pizza")

main()
