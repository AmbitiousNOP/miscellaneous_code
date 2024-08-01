#!/usr/bin/env python
from collections import namedtuple

# create named tuple class with specified fields
# (could also provide fieldnames as iterable)
Knight = namedtuple('Knight', 'name title color quest comment')

# create named tuple instance (must specify all fields)
k = Knight('Bob', 'Sir', 'green', 'whirled peas', 'Who am i?')

print(k.title, k.name, k[1], k[0])  # access fields by name or index
print("*" * 30)
knights = {}  # initialize dict for knight data
with open('../../data/knights.txt') as knights_in:
    for line in knights_in:
        flds = line.rstrip().split(':')

        # add knight tuple to dictionary where key is knight name
        knights[flds[0]] = Knight(*flds)

# iterate over dictionary; info is knight tuple
for key, knight in knights.items():
    print('{0} {1}: {2}'.format(knight[1], key, knight.color))
