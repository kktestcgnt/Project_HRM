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

# Calling a class method inside __init__
class Employee:
    # This is class variable or class attribute
    emp_department = "Testing"

    def __init__(self, name, empid):
        self.display(name, empid)

    def display(self, x, y):   # Remove self and run and check
        print(x)
        print(y)


obj_employee = Employee("admin", 12345)
