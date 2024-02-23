"""
from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 'qwerty'
    WINTER = 4
    ID = 0
    NAME = 1
class Data(Enum):
    ID = 0
    NAME = 1
    DES = 2
x = ('7369', 'SMITH', 'JOHN')
ID = Season['NAME']
NAME = Season['NAME'].value
# print("The enum member associated with value 2 is : ", Season('qwerty').name)
# print("The enum member associated with name AUTUMN is : ", Season['NAME'].value)
print(x[Data['DES'].value])
"""
import pytest

# ===========================================================================================================
"""
list1 = ['ID', 'NAME', 'LNAME', 'Des']
list2 = 'qwertyui'

v1 = 'qwerty'
v2 = 'asdfg'


def display(*args):

    print(args)
#     print(*args, len(*args), type(*args))
#     print(args, len(args), type(args))
#     print(*args[0])
    # x = *args
    print(len(args))
    for each in args:
        print(each)

    # for each in *args:
    #     print(each)


display(v1, v2)

# def display2(args):
#     print(args, len(args))
#
#
# display2(list1, list2)
# display2(list2)
"""


# ===========================================================================================================

@pytest.fixture
def check_output():
    x = 5
    print(x)

    def display():
        print('in display function')
        return x

    yield display()
    print('end of function')


def display_check(check_output):
    print(check_output)
    print('in display check function')


display_check()
