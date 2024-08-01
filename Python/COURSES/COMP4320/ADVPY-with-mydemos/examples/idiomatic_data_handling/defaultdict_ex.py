#!/usr/bin/env python

from collections import defaultdict
import collections
def1 = defaultdict(int)
def1['a']    = 3
def1['a'] += 1
def1['b'] +=2

dd = defaultdict(lambda: 10)  # create defaultdict with function that returns 0

dd['spam'] = 10  # assign some values to the dict
dd['eggs'] = 22

print(dd['spam'], dd['eggs'])
print(dd['foo'])  # missing key 'foo' invokes function and returns 0


od = collections.OrderedDict(((2, 'ken'), (1,'jen'), (3, 'ben')))
od[4] = 'len'
print(od)
d1 = dict(((2, 'ken'), (1,'jen'), (3, 'ben')))
d1[4] = 'len'
print(d1)