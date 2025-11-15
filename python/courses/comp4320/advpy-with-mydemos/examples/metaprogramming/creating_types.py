#!/usr/bin/env python
def function_1(self):  # create method (not inside a class - could be a lambda)
    print("Hello from f1()")


def function_2(self):  # create method (not inside a class - could be a lambda)
    print("Hello from f2()")


# create class using type()
# parameters are class name, base classes, dictionary of attributes
NewClass = type("NewClass", (), {
    'hello1': function_1,
    'hello2': function_2,
    'color': 'red',
    'state': 'Ohio'
})
