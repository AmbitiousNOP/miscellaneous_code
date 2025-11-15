from functools import *
from operator import *

def add(x, y):
    return x + y

print(add(1,2))

add1 = partial(add, 4)
print(add1(6))
print(add1(10))

lst = list(map (add1, [1, 2, 3, 4, 5]))
print(lst)

seven = partial(add1, 3)
print(seven())


str1 = "Hello, Python"
helloStr = partial(str1.replace, "Python")
str2 = helloStr("Tutorialspoint")
str3 = helloStr("Java")

print()