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
