#!/usr/bin/env python
from itertools import groupby


def get_state(r):
    return r[6]


count_of = {}
with open('../../data/presidents.txt') as pres_in:
    results = groupby(sorted(map(lambda r: r.split(':'), pres_in),
                             key=get_state), key=get_state)

for state, presidents in results:
    print(f'{state:16}: {len(list(presidents))}')
