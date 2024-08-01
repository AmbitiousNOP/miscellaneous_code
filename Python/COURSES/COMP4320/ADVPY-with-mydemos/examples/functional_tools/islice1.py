# Python program to demonstrate
# the working of islice

from itertools import islice


# Slicing the range function   list(range(20))[:5]
for i in islice(range(20), 5):
	print(i)

	
li = [2, 4, 5, 7, 8, 10, 20]

# Slicing the list
print(list(islice(li, 1, 6, 2)))
print(list(islice(li, 1, 16, 2)))  # OK - where stop is > length
# Slicing a range
for i in islice(range(20), 1, 5):
	print(i)
 
 # Slicing a range
for i in islice(range(20), 1, 5, 2):
        print(i)
