#!/usr/bin/env python
'''
This is the doc string for the module/script.
'''
# standard library imports
import sys

# third party module imports

# local module imports

# constants (AKA global variables -- keep these to a minimum)


def main(args):
    '''
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    '''
    function1()


def function1():
    '''
    This is the docstring for function1().

    :return: None
    '''
    pass


if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()
