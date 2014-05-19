#!/usr/bin/env python3

# -----------
# Employee.py
# -----------

""" ----------------------------------------------------------------------
Replace Type Code with State/Strategy (227)
Replace Conditional with Polymorphism (225)
"""

from unittest import main, TestCase

class Employee :
    ENGINEER = 0
    SALESMAN = 1
    MANAGER  = 2

    def __init__ (self, salary, type_code) :
        self.salary = salary
        self.set_type_code(type_code)

    def get_pay (self) :
        if self.type_code == Employee.ENGINEER :
            return self.salary

        if self.type_code == Employee.SALESMAN :
            return self.salary + 10000

        if self.type_code == Employee.MANAGER :
            return self.salary + 20000

    def get_type_code (self) :
        return self.type_code

    def set_type_code (self, type_code) :
        self.type_code = type_code

class UnitTests (TestCase) :
    def test_1 (self) :
        x = Employee(50000, Employee.ENGINEER)
        self.assertEqual(x.get_pay(), 50000)

    def test_2 (self) :
        x = Employee(50000, Employee.SALESMAN)
        self.assertEqual(x.get_pay(), 60000)

    def test_3 (self) :
        x = Employee(50000, Employee.MANAGER)
        self.assertEqual(x.get_pay(), 70000)

main()
