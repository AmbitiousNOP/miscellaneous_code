#!/usr/bin/env python
import inspect


def main():
    fmt = "{:>10}:  {:10}{:10}{:10}{:10}"
    print(fmt.format("Reference", "Module?", "Function?", "Class?", "Method?"))
    for thing in (inspect, Spam, Spam().eggs, ham):
        print(fmt.format(thing.__name__,
              str(inspect.ismodule(thing)),    # test for module
              str(inspect.isfunction(thing)),  # test for function
              str(inspect.isclass(thing)),     # test for class
              str(inspect.ismethod(thing))))     # test for method

    # get argument specifications for a function
    argspec = inspect.getfullargspec(ham)
    print("\nFunction spec for ham:", argspec)

    # get frame (function call stack) info
    frame = inspect.getframeinfo(inspect.currentframe())
    print("\nCurrent frame:", frame)


class Spam:                                  # defines a class
    def eggs(self):
        pass


def ham(p1, p2='a', *p3, p4, p5='b', **p6):  # define a function
    print(p1, p2, p3, p4, p5, p6)


if __name__ == '__main__':
    main()
