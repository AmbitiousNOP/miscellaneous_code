#!/usr/bin/env python
# (c) 2016 John Strickler
#
import sys
from functools import reduce
from itertools import chain

files = map(open, sys.argv[1:])
print(reduce(lambda a, b: a + 1, chain.from_iterable(files), 0))
