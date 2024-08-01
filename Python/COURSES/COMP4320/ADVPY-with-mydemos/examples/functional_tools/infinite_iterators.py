#!/usr/bin/env python
from itertools import islice, count, cycle, repeat


def main():
    for i in count(0, 10):             # count by tens starting at 0 forever
        if i > 50:
            break                      # without a check, will never stop
        print(i, end=' ')
    print("\n")

    # saner, using islice to get just the first 6 results
    for i in islice(count(0, 10), 6):
        print(i, end=' ')
    print("\n")

    giant = ['fee', 'fi', 'fo', 'fum']

    # cycle over values in list forever (use islice to stop)
    for i in islice(cycle(giant), 100):
        print(i, end=' ')
    print("\n")

    # repeat value 10 times (default is repeat forever)
    for i in repeat('tick', 10):
        print(i, end=' ')
    print("\n")


if __name__ == '__main__':
    main()
