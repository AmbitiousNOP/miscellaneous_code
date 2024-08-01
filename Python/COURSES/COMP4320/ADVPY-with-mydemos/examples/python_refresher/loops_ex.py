#!/usr/bin/env python

# creaet a list
colors = ['red', 'green', 'blue', 'purple', 'pink', 'yellow', 'black']

for color in colors:  # loop over list
    print(color)
print()

with open('../data/mary.txt') as MARY:  # open text file for reading
    for line in MARY:                   # loop over lines in file
        print(line, end='')             # print line without extra newline
print()

while True:  # loop 'forever'
    name = input("What is your name? ")  # read input from keyboard
    if name.lower() == 'q':
        break  # exit loop
    print("Welcome,", name)
