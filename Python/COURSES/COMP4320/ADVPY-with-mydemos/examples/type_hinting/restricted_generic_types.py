#!/usr/bin/env python
from typing import TypeVar, Sequence
Choice = TypeVar('Choice', int, str)  # Restrict the choice to int or str
Numeric = TypeVar('Numeric', int, float)


def first(numbers: Sequence[Numeric]) -> Numeric:
    return numbers[0]


def third(coll: Sequence[Choic
                         e]) -> Choice:
    return coll[2]


print(first([99, 77, 55, 88]))

print(third([1, 2, 3]))
print(third(("A", "B", "C", "D")))

# Python is ok with these two - but mypy will complain
print(third(["A", '1', "B", '2']))
print(third([2.3, 5.4, 6.9]))
