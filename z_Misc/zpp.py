"""
Class is nothing but a blueprint/template which describes the behavior of its Objects

Python coding rules/styles is defined by PEP (Always check PEP version before any interview)

self is an object of the class and is used to access the methods and attributes of the class
__init__ is the default method or ( Constructor )
"""
import time

# Constructor
"""
class Employee:
    def __init__(self):
        print("init method")


obj_Employee = Employee()
# Output = init method
"""

# Basic Class
"""
class Employee:

    # This is class variable or class attribute
    emp_department = "Testing"

    def __init__(self, name, empid):
        # These are the Instance or (Global) variables. These change from object to object of same class
        self.name = name
        self.empid = empid

    def display(self):
        print(self.name)
        print(self.empid)


obj_employee = Employee("admin", 12345)

# We see None in output because we are printing the output of display method which is not having any return value.
# Add a return value to display method, return value will be printed in place of None
print(obj_employee.display())
print(obj_employee.emp_department)

# obj_employee1 = Employee()
# print(obj_employee1.display())
"""
# ====================================================================
"""
# Calling a class method inside __init__
class Employee:
    # This is class variable or class attribute
    emp_department = "Testing"

    def __init__(self, name, empid):
        self.display(name, empid)

    def display(self, x, y):  # Remove self and run and check
        print(x)
        print(y)


obj_employee = Employee("admin", 12345)
"""
# ===========================================================================
"""
# count = 0
# Operating overload (Polymorphism) --------->
class MathOperation:

    # global count

    def __init__(self, val1):
        self.val = val1
        # count = count + 1
        print(self.val)

    # def __add__(self, other):
    #     print("add : ", self.val)
    #     print("add : ", other.val)
    #     return self.val + other.val

    # def __sub__(self, other):
    #     return self.val - other.val


obj1_mathoperation = MathOperation(5)
obj2_mathoperation = MathOperation(8)

print(obj1_mathoperation + obj2_mathoperation)
"""

# ====================================================================
"""
# Method overload (Polymorphism) --------->

class MethodOverloading:

    def addition(self, val1, val2):
        return val1 + val2

    def addition(self, val1, val2, val3):
        return val1 + val2 + val3


obj1_methodoverload = MethodOverloading()
obj1_methodoverload.addition(5, 2)

"""

# ====================================================================
"""
# Multiple Inheritance --------->
# Here Precedence is given to left most inherited class

class Parent1:

    def display(self):
        print("In Parent1")


class Parent2:

    def display(self):
        print("In Parent2")


class Child(Parent1, Parent2):
    pass


obj_child = Child()
obj_child.display()

# Child(Parent1, Parent2) - Output : In Parent1
# Child(Parent2, Parent1) - Output : In Parent2
"""


# ====================================================================
"""
# Multilevel Inheritance ---->
# Method OverRiding ---->
# Here Precedence is given from bottom to top (from child to its immediate Parent)

class GrandParent:
    def display(self):
        print("from GrandParent")


class Parent(GrandParent):
    def display(self):
        super().display()
        print("from Parent")


class Child(Parent):
    def display(self):
        super().display()
        print("from Child")
        GrandParent.display(self)


obj_child = Child()
obj_child.display()

# Output -
# from GrandParent
# from Parent
# from Child
# from GrandParent
"""

