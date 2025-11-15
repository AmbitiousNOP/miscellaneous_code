#!/usr/bin/env python

count_of = {}
with open("../../data/presidents.txt") as pres_in:
    for rec in pres_in:
        flds = rec.split(":")
        state = flds[6]
        count_of[state] = count_of.get(state, 0) + 1

for state, count in sorted(count_of.items()):
    print("{:16} {:2}".format(state, count))
