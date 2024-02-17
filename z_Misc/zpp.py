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

# ====================================================================


"""
----------------- xxxxxxxxxxxx -----------------------
# class MyClass:
#     class_var = "This is class variable"
# 
#     def __init__(self, arg1):
#         self.arg1 = arg1
# 
#     def static_method_one():
#         print('This is static class')
# 
#     def static_method_two(x, y):
#         return x + y
# 
#     @staticmethod
#     def static_method_three():
#         print('from static method three')
#         # print(self.arg1)
#         # print(MyClass.arg1)
# """

# Traceback (most recent call last):
#   File "H:\Python_Projects\Project_HRM\z_Misc\zpp.py", line 207, in <module>
#     obj_myclass.static_method_three()
#   File "H:\Python_Projects\Project_HRM\z_Misc\zpp.py", line 193, in static_method_three
#     print(MyClass.arg1)
#           ^^^^^^^^^^^^
# AttributeError: type object 'MyClass' has no attribute 'arg1'
# """
#
#         print(MyClass.class_var)
#
#
# MyClass.static_method_one()
# print(MyClass.static_method_two(3, 4))
# obj_myclass = MyClass(5)
#
# # obj_myclass.static_method_one()
# """
# Output - Traceback (most recent call last):
#   File "H:\Python_Projects\Project_HRM\z_Misc\zpp.py", line 189, in <module>
#     obj_myclass.static_method_one()
# TypeError: MyClass.static_method_one() takes 0 positional arguments but 1 was given
#
# obj_myclass.static_method_three()
# """
#
#
# class ChildOne(MyClass):
#     pass
#
#
# # obj_childone = ChildOne()
# # Traceback (most recent call last):
# #   File "H:\Python_Projects\Project_HRM\z_Misc\zpp.py", line 214, in <module>
# #     obj_childone = ChildOne()
# #                    ^^^^^^^^^^
# # TypeError: MyClass.__init__() missing 1 required positional argument: 'arg1'
#
# class ChildTwo(ChildOne):
#
#     def __init__(self):
#         pass
#
#
# obj_childtwo = ChildTwo()
# obj_childtwo.static_method_three()
#
# ----------------- xxxxxxxxxxxx -----------------------
# """

# class LearnClassMethods:
#     class_attr = 'This is class attribute'
#
#     def class_method_one(self):
#         print(self.class_attr)
#
#     @classmethod
#     def class_method_two(cls):
#         print("Hello!")
#         print(LearnClassMethods.class_attr)
#
#
# obj_learn_class_methods = LearnClassMethods()
# obj_learn_class_methods.class_method_one()
#
# print(obj_learn_class_methods.class_attr)
#
# obj_learn_class_methods.class_method_two()

# Output -
# ===========
# Traceback (most recent call last):
#   File "H:\Python_Projects\Project_HRM\z_Misc\zpp.py", line 263, in <module>
#     obj_learn_class_methods.class_method_two()
# TypeError: LearnClassMethods.class_method_two() takes 0 positional arguments but 1 was given
# ===========


# =-=============================================================================
"""
class LearnClassMethodsChild:

    count = 0

    # def __init__(self, arg1):
    #     self.arg1 = arg1

    @classmethod
    def class_method_three(cls):
        cls.count = cls.count + 1
        print("In class_method_three")
        print('cls count : ', cls.count)
        cls.my_static()

    @staticmethod
    def my_static():
        print('Count = ', LearnClassMethodsChild.count)
        if LearnClassMethodsChild.count > 3:
            exit(0)
        print('In my_static')
        LearnClassMethodsChild.count = LearnClassMethodsChild.count + 1
        # LearnClassMethodsChild.class_method_three()


class LearnClassMethodsNewChild(LearnClassMethodsChild):
    def display(self):
        print('from LearnClassMethodsNewChild -- count : ', self.count)


obj_learn_class_methods_child = LearnClassMethodsChild()
obj_learn_class_methods_child.class_method_three()
# obj_learn_class_methods_child.my_static()
obj_learn_class_methods_new_child = LearnClassMethodsNewChild()
obj_learn_class_methods_new_child.display()

"""

"""
# Encapsulation
# ==============

# Access specifiers -
# public - name - this is accessible for all
# protected - _name - this is accessible to the class where it is defined and its derived classes (Inheritance)
# private - __name - this is accessible only to the class where it is defined

class EncapsulationClass:
    public = 'public'
    _protected = 'protected'
    __private = 'private'

# same is applicable for methods also.
# def public():
# def _protected():
# def __private():


obj_encap = EncapsulationClass()
print(obj_encap.public)
print(obj_encap._protected)
# print(obj_encap.__private)
print(_EncapsulationClass._obj_encap.__private)
"""

"""
# Data Class
# ============

from dataclasses import dataclass


@dataclass
class Data:
    name: str
    roll_no: int
    id: int
    salary: float


obj_data1 = Data('data', 22, 5678, 23456.987)
print(obj_data1)
obj_data2 = Data('data', 22, 5678, 23456.987)
# print(obj_data2)
if obj_data1 == obj_data2:
    print('inside if')
    print(obj_data2)
obj_data3 = 5
print(isinstance(obj_data1, Data))
print(isinstance(obj_data3, Data))

# How do you find out an object belongs to particular class or not.
# Ans: using method instance()
"""

"""
class ABC:
    abc_attr = 3


obj_abc = ABC()
print(obj_abc.abc_attr)
obj_abc.abc_attr = 'qwerty'
print(obj_abc.abc_attr)

setattr(obj_abc, 'abc_attr', 1234)
print(obj_abc.abc_attr)

setattr(obj_abc, 'abc_attr', 'asdfgh')
print(obj_abc.abc_attr)

my_dict = {'a': 1, 'b': 'abc'}
print(my_dict['b'])
print(my_dict.get('a'))

for key, value in my_dict.items():
    print(key, value)
"""

# Abstract methods
# ===================

from abc import ABC, abstractmethod


class AbstractClassLearn(ABC):

    @abstractmethod
    def display(self):
        pass


class AbstractClassLearn2(AbstractClassLearn):
    def display1(self):
        print("abstract child display")


# obj_abc_class = AbstractClassLearn()
# obj_abc_class.display()
obj_abc_class2 = AbstractClassLearn2()
obj_abc_class2.display1()
