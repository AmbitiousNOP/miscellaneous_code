#!/usr/bin/env python
from itertools import product, permutations, combinations


def main():
    SUITS = 'CDHS'
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    # Cartesian product
    # (match every item in one list to every item in the other list)
    cards = product(SUITS, RANKS)
    print(list(cards), '\n')

    # reverse order and concatenate elements using list comprehension
    cards = [f"{suit}{rank}" for rank, suit in product(SUITS, RANKS)]
    print(cards, '\n')

    giant = ['fee', 'fi', 'fo', 'fum']

    # all distinct combinations of  items taken 2 at a time
    result = combinations(giant, 2)
    print(list(result), "\n")

    # all distinct permutations of items taken 2 at a time
    result = permutations(giant, 2)
    print(list(result), "\n")

if __name__ == '__main__':
    main()
