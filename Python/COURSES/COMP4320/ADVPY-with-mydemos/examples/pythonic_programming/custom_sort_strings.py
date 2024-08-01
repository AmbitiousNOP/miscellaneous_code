#!/usr/bin/env python


def ignore_case(item):  # Parameter is one element of iterable to be sorted
    return item.lower()  # Return value to sort on instead  of item


def by_length_then_name(item):
    # Key functions can return tuple of values to compare, in order
    # Since lists and tuples automtically sort to the n-th element level
    return (len(item), item.lower())


fruit = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
         "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear",
         "banana", "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry"]

fs1 = sorted(fruit, key=ignore_case)  # register function to use to sort
print("Ignoring case:")
print(" ".join(fs1), end="\n\n")

fs2 = sorted(fruit, key=by_length_then_name)
print("By length, then name:")
print(" ".join(fs2))
print()
