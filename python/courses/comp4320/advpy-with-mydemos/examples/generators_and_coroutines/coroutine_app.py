#!/usr/bin/env python
from coroutine_example import coroutine
c = coroutine()  # Create instance of coroutine

print(type(c), c)  # Print coroutine object
next(c)  # Prime (start) the coroutine

for letter in "alpha", "beta", 'gamma':
    c.send(letter)  # Send in data
print()
#c.close()
#c.send("oops")