#!/usr/bin/env python
from functools import wraps


def main():
    hello('hello', 'world')  # call new function
    print()

    hello('hi', 'Earth')
    print()

    hello('greetings')
    

# decorator function -- expects decorated (original) function as a parameter
def debugger(old_func):

    @wraps(old_func)  # preserves name of original function after decoration
    def new_func(*args, **kwargs):  # replacement; with generic params
        print("*" * 40)                                # new functionality
        print("** function", old_func.__name__, "**")  # new functionality

        if args:                                       # new functionality
            print("\targs are ", args)
        if kwargs:                                     # new functionality
            print("\tkwargs are ", kwargs)

        print("*" * 40)                                # new functionality

        return old_func(*args, **kwargs)  # call the original function

    return new_func                       # return the new function object


@debugger  # apply the decorator to a function
def hello(greeting, whom='world'):
    print("{}, {}".format(greeting, whom))


if __name__ == '__main__':
    main()
