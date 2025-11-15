#!/usr/bin/env python
from operator import add, mul
from functools import reduce


def main():
    values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    strings = ['fi', 'fi', 'fo', 'fum']

    # continually reduce by adding to initial value of first element
    print("result is", reduce(add, values))

    # continually reduce by adding to initial value of 1000
    print("result is", reduce(add, values, 1000))

    # continually reduce by multiplying by initial value of 1
    print("result is", reduce(mul, values, 1))

    # continually reduce by adding to initial string of ""
    print("result is", reduce(add, strings, ""))

    # continually reduce by adding uppercase to initial string of ""
    result = reduce(add, list(map(str.upper, strings)), "")
    print("result is", result)


if __name__ == '__main__':
    main()
