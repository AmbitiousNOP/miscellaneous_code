#!/usr/bin/env python

with open("../../data/mary.txt") as mary_in:
    print(mary_in.closed)
    # Get unique words from file
    # Only one line (ln) is in memory at any point
    # Skip "empty" words
    s = { w.lower() for ln in mary_in.readlines() for w in ln.split() if w }
#mary_in.close()
print(mary_in.closed)
print(2 * '\n')
print(s)
