#!/usr/bin/env python
from creating_types import NewClass


def main():
    n1 = NewClass()  # create instance of new class
    print(type(n1))
    n1.hello1()      # call instance method
    n1.hello2()
    print(n1.color)  # access class data
    print()

    # create subclass of first class
    SubClass = type("SubClass", (NewClass,), {'fruit': 'banana'})   
    s1 = SubClass()  # create instance of subclass
    print(type(s1))

    s1.hello1()      # call method on subclass
    print(s1.color)  # access class data
    print(s1.fruit)


if __name__ == '__main__':
    main()
