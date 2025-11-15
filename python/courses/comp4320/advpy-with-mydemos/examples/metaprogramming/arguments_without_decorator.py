#!/usr/bin/env python
from spam_decorator_with_args import spam


def main():
    global ham
    print(ham())
    ham = spam(2, 3)(ham)
    print(ham())


def ham():
    return "Ham"


if __name__ == '__main__':
    main()
