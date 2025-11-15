#!/usr/bin/env python
from pprint import pprint

# nested data structure
data = {
    'part1': [['a', 'b', 'c'], ['d', 'e', 'f']],
    'part2': {'red': 55, 'blue': [8, 98, -3],
              'purple': ['Chicago', 'New York', 'L.A.']},
    'part3': ['g', 'h', 'i']
}

print('Without pprint:', data, "#" * 30, sep="\n")

print('With pprint:')
pprint(data)                  # pretty-print
print()

print('With pprint (depth=2):')
pprint(data, depth=2)         # only print top two levels of structure
print()
