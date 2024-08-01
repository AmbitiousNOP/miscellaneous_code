#!/usr/bin/env python
import sys
from functools import reduce
from itertools import chain


line_count = 0   # INCREMENTING COUNT FOR # OF LINES IN EACH FILES
word_count = 0
def calc(a, b):
    # b will be ignored - its dummy to satify reduce(func, iterable ) 2 param requirement
    global line_count 
    global word_count
    line_count += 1
    word_count += len(b.rstrip().split())

# generate map object that contains iterable of fileObjects
files = map(open, sys.argv[1:])  # python3 count_demo.py file1.txt file2.txt 

# test 
# loop through files to confirm all files opened
# do not leave uncommented when continue next 
# or map object will be left at end/empty
'''
for f in files:
    print(f)
'''
# generate chain object (generator)
# when we loop through it with reduce later, we will count the # of iterations
chain1 = chain.from_iterable(files)

# test to confirm chain is iterating
# do not leave uncommented when continue next or map map object will be at end of items
'''
for line in ch1:
    print(type(line), line)
'''
reduce(calc, chain1, 0)  # init count to 0 and increment for each iteration of ch1
print(line_count,word_count)


# THE TEARSE SOLUTION
# the 'b' param here is a dummy to fill in the 2nd param if func that reduce needs
# patam 'a' is the counter cooresponding to my line_count counter in verbose code above
files = map(open, sys.argv[1:])
print(reduce(lambda a, b: a + 1, chain.from_iterable(files), 0))