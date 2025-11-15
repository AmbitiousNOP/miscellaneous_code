#!/usr/bin/env python
from spam_decorator import spam


def main():
    global ham
    print(ham())
    ham = spam(ham)
    print(ham())


def ham():
    return "Ham"


if __name__ == '__main__':
    main()
