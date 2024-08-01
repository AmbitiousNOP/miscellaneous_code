#!/usr/bin/env python
for number in [4, 8, 9, 3, 5, 1]:
    print(number)

# The above for loop is simply syntactic sugar for the following code
iterator = iter([4, 8, 9, 3, 5, 1])  # Really invokes list.__iter__()
try:
    while True:
        number = next(iterator)  # Really invokes iterator.__next__()
        print(number)
except StopIteration:
    pass
