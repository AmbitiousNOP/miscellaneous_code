#!/usr/bin/env python

def main():
    strings = ['wombat', 'koala', 'kookaburra', 'blue-ringed octopus']

    print(list(map(str.upper, strings)))  # Map list to upper case
    print(list(map(len, strings)))  # Map to list of string lengths

    #  Using a list comprehension, which is usually simpler than map()
    print([s.upper() for s in strings])
    print("=" * 30)
    fancy_mapping()


def fancy_mapping():
    tests = {"Sally": (89, 78, 99, 88, 92, 98, 95, 78, 88),
             "Doug": (68, 87, 72, 60, 80, 65, 87),
             "Kesha": (98, 87, 99, 78, 99, 80, 98, 50),
             "John": (89, 78, 99, 88, 92, 99, 95, 88, 95, 99)}
    # Find the average of the first test taken by each student,
    # followed by the second test taken by each, ... to the length
    # of the shortest iterable passed to map()
    x = map(averages, *tests.values())
    print("Averages:", list(x))


def averages(*grades):
    qty = len(grades)
    return sum(grades)/qty


if __name__ == '__main__':
    main()
