#!/usr/bin/env python

color = 'blue'
animal = 'iguana'

# {} placeholders are autonumbered by default, starting at 0
# this corresponds to the parameters to format()
print('{} {}'.format(color, animal))

fahr = 98.6839832

# Formatting directives start with ':'
# .1f means format floating point with one decimal place
print('{:.1f}'.format(fahr))

value = 12345

# {} placeholders can be manually numbered to reuse parameters
print('{0:d} {0:04x} {0:08o} {0:016b}'.format(value))

data = {'A': 38, 'Z': 99, 'B': 127, 'C': 9}
nums = [13,4,5]


    
for letter, number in sorted(data.items()):
    # 4d means format decimal integer in a field 4 characters wide
    print("{} {:4d}".format(letter, number))
