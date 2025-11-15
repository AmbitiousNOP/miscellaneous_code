#!/usr/bin/env python
from pprint import pprint    # import prettyprint function

spam = 42                    # global variables
ham = 'Smithfield'


def main():
    eggs('mango')


def eggs(fruit):             # function parameters are always local
    name = 'Lancelot'        # local variable
    idiom = 'swashbuckling'  # local variable
    print("Globals:")
    pprint(globals())        # globals() returns dict of all globals
    print()
    print("Locals:")
    pprint(locals())         # locals() returns dict of all locals


if __name__ == '__main__':
    main()
