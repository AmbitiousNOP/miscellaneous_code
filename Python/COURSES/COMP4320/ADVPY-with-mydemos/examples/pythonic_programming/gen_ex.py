#!/usr/bin/env python

limit = 10**4

# sum the squares of a list of numbers
# using list comprehension, entire list is stored in memory
s1 = sum([x * x for x in range(limit)])

# only one square is in memory at a time with generator expression
s2 = sum(x * x for x in range(limit))
print(s1, s2)
print()

page = open("../../data/mary.txt")
# Only one line in memory at a time; max() iterates over generated values
m = max(len(line) for line in page)
page.close()
print(m)
