#!/usr/bin/env python
import pickle
from collections import namedtuple

fields = 'term firstname lastname birthplace birthstate party'
President = namedtuple('President', fields)

# note: definition of President should be
# in module shared between read_potus_info.py
# and save_potus_info.py

with open('potus.pic', 'rb') as POTUS:
    presidents = pickle.load(POTUS)

for p in presidents:
    print("{} {}".format(p.firstname, p.lastname))
