#!/usr/bin/env python
from functools import wraps  # Preserves properties of original function


def main():
    a = spam()
    b = ham()
    print(a, b)


def multiply(multiplier):    # actual decorator - receives decorator parameters

    def deco(old_func):      # inner decorator - receives decorated function

        @wraps(old_func)     # retain name, etc. of original function
        def new_func(*args, **kwargs):    # replacement function for orignal
            # call original function and get return value
            result = old_func(*args, **kwargs)

            # multiple result of original function by multiplier
            return result * multiplier

        return new_func  # new funtion returnd by deco()

    return deco  # deco fucntion returned by mutliply()


@multiply(4)
def spam():
    return 5


@multiply(10)
def ham():
    return 8


if __name__ == '__main__':
    main()
