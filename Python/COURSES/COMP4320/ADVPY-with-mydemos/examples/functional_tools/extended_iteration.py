#!/usr/bin/env python
from itertools import chain, takewhile, dropwhile


def main():
    spam, ham = ['alpha', 'beta', 'gamma'], ['delta', 'epsilon', 'zeta']
    # treat spam and ham as a single iterable
    print_iterable(chain(spam, ham))

    eggs = [spam, ham]
    # treat all elements of eggs as a single iterable
    #iter_eggs = list(chain.from_iterable(eggs))   # debug code
    print_iterable(chain.from_iterable(eggs))

    fruits = ["pomegranate", "cherry", "apricot", "date", "apple", "lemon",
              "kiwi", "orange", "lime", "watermelon", "guava", "papaya", "fig",
              "pear", "banana", "tamarind", "persimmon", "elderberry", "peach"]
    # iterate over elements of fruits as long as length of current item > 4
    print_iterable(takewhile(lambda f: len(f) > 4, fruits))

    # iterate over elements of  fruits as long as fruit does not start with 'k'
    print_iterable(takewhile(lambda f: f[0] != 'k', fruits))

    values = [5, 18, 22, 31, 44, 75, 59, 61, 66, 70, 72, 78, 90, 99]
    # skip over elements as long as value is < 50, then iterate over rest
    print_iterable(dropwhile(lambda f: f < 50, values))


def print_iterable(iter_obj):  # helper function to print each iterable
    print(*iter_obj, sep=' ', end="\n\n")


if __name__ == '__main__':
    main()
