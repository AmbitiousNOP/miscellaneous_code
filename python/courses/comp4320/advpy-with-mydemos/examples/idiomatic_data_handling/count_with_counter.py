#!/usr/bin/env python

from collections import Counter

counts = Counter()  # create Counter object (defaults to 0 for missing keys)

with open("../../data/breakfast.txt") as breakfast_in:
    for line in breakfast_in:
        item = line.rstrip()  # remove EOL from line
        counts[item] += 1     # increment count for current item

for item, count in counts.items():  # iterate over results
    print(item, count)
