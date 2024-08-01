#!/usr/bin/env python
import copy

data1 = [[1, 2, 3], [4, 5, 6]]
data2 = copy.deepcopy(data1)

data2[0].append(99)

# Outer list is still a unique copy
print("data1:", "id:", id(data1), data1)
print("data2:", "id:", id(data2), data2)
print()

# Nested lists are now a unique copy also
print("Nested list ids of data1")
print("\tid of data1[0]: ", id(data1[0]))
print("\tid of data1[1]: ", id(data1[1]))
print()
print("Nested list ids of data2")
print("\tid of data2[0]: ", id(data2[0]))
print("\tid of data2[1]: ", id(data2[1]))
