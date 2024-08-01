#!/usr/bin/env python

fruits = ['Pomegranate', 'Apple', 'Mango', 'KIWI', 'apricot', 'Watermelon']

# The lambda function is passed one fruit and returns it in lower case
fruits.sort(key=lambda e: (len(e), e.lower()))
print(" ".join(fruits))

# the top level max() function also allows a function to be passed as a key.
print(max(fruits), max(fruits, key=lambda f: len(f)))
# Though it is much simpler in this case to simply rely on th ebuild in len
print(max(fruits, key=len))
