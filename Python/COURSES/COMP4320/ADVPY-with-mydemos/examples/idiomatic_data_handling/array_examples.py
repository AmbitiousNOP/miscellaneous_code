#!/usr/bin/env python
from sys import getsizeof
from array import array
from random import randint

values = [randint(1, 30000) for i in range(1000)]  # Create list of 1000 ints

print(f'Size of integer list: {getsizeof(values)}\n')

fmt = "[{}, {}, {}, {}, {}, ...]"

for datatype in 'i', 'h', 'L', 'Q', 'd':
    data_array = array(datatype, values)  # Create array of specified type
    print(f'Size of {datatype} array: {getsizeof(data_array):,}  Contents:',
          fmt.format(*data_array[:5]))  # Note memory usage
