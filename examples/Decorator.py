#!/usr/bin/env python3

# ------------
# Decorator.py
# ------------

class Pizza :
    def cost (self) :
        return 7

    def __str__ (self) :
        return "Pizza"

class PizzaDecorator :
    def __init__ (self, p) :
        self.p = p

class CheesePizzaDecorator (PizzaDecorator) :
    def cost (self) :
        return self.p.cost() + 1

    def __str__ (self) :
        return "Cheese " + str(self.p)

class SausagePizzaDecorator (PizzaDecorator) :
    def cost (self) :
        return self.p.cost() + 2

    def __str__ (self) :
        return "Sausage " + str(self.p)

print("Decorator.py")

p = Pizza()
assert p.cost() == 7
assert str(p)   == "Pizza"

p = CheesePizzaDecorator(Pizza())
assert p.cost() == 8
assert str(p)   == "Cheese Pizza"

p = SausagePizzaDecorator(CheesePizzaDecorator(Pizza()))
assert p.cost() == 10
assert str(p)   == "Sausage Cheese Pizza"

p = CheesePizzaDecorator(SausagePizzaDecorator(CheesePizzaDecorator(Pizza())))
assert p.cost() == 11
assert str(p)   == "Cheese Sausage Cheese Pizza"

print("Done.")
