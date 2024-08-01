#!/usr/bin/env python
"""Basic sorting example"""

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
          "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear",
          "banana", "Tamarind", "persimmon", "elderberry", "peach", "grape",
          "lychee", "BLUEberry"]

sorted_fruit = sorted(fruits)  # sorted() always returns a list
# determine length of longest string in list

fmt = "{:18}"
for counter, fruit in enumerate(sorted_fruit):
    
    print(fmt.format(fruit), end='')
    if counter % 4 == 3:
        print()
    #print(counter, fruit)
    
print()
