#!/usr/bin/env python

import sys

name = 'Tim'
count = 5
avg = 3.456
info = 2093
result = 38293892

# < means left justify (default for non-numbers)
# 10 is the minimum field width, s formats a string
print(f'Name is [{name:<10s}]')


print(f'Name is [{name:>10s}]')  # > means right justify

# .2f means round a float to 2 decimal points
print(f'count is {count:03d} avg is {avg:.2f}')

# d is decimal, o is octal, x is hex
print(f'info is {info} {info:d} {info:o} {info:x}')

# , means add commas to numeric value
print(f'${result:,d}')

city = 'Orlando'
temp = 85

# parameters can be selected by name instead of position
print(f'It is {temp} in {city}')
