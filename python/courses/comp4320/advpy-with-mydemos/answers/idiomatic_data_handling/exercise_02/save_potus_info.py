#!/usr/bin/env python
import csv
import pickle
from collections import namedtuple

fields = 'id lastname firstname birthdata dod county state termbegin termend party'
President = namedtuple('President', fields)

presidents = []
with open('../../data/presidents.csv') as PRES:
    rdr = csv.reader(PRES, delimiter=':')
    for row in rdr:
        pres = President(*row)
        presidents.append(pres)

print(presidents[15].firstname, end=' ')
print(presidents[15].lastname, end=' ')
print(presidents[42].party)

with open('potus.pic', 'wb') as POTUS:
    pickle.dump(presidents, POTUS)
