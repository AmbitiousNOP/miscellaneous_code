#!/usr/bin/env python

values = ['a', 'b', 'c', 'd', 'e']  # *values* has 6 elements
_, a,b, *_ = values
x, y, *z = values  # *z takes all extra elements from iterable
print("x: {}    y: {}    z: {}".format(x, y, z))
print()

x, *y, z = values  # *{y takes all extra elements from iterable
print("x: {}    y: {}    z: {}".format(x, y, z))
print()

*x, y, z = values  # *x takes all extra elements from iterable
print("x: {}    y: {}    z: {}".format(x, y, z))
print()

people = (('Bill', 'Gates', 'Microsoft'), ('Steve', 'Jobs', 'Apple'),
          ('Paul', 'Allen', 'Microsoft'), ('Larry', 'Ellison', 'Oracle'),
          ('Mark', 'Zuckerberg', 'Facebook'), ('Sergey', 'Brin', 'Google'),
          ('Larry', 'Page', 'Google'), ('Linux', 'Torvalds', 'Linux'))

for *name, _ in people:  # *name* gets all but the last field
    #print(name)
    print("{} {}".format(*name))
print()
