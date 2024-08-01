#!/usr/bin/env python
class MaxList(list):
    def __init__(self, max_size):
        self._max_size = max_size

    def append(self, value):
        if len(self) == self._max_size:
            raise IndexError("Maximum size reached")
        else:
            super().append(value)

    def insert(self, idx, value):
        if len(self) == self._max_size:
            raise IndexError("Maximum size reached")
        else:
            super().insert(idx, value)
            
m = MaxList(3)

m.append('a')
m.append('b')
m.append('c')

try:
    m.append('d')
    m.insert(1,99)
except IndexError as err:
    print(err)
else:
    print(m)
