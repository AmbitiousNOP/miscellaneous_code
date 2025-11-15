# Program for creating a list of
# even and odd list of integers
# using count()

from itertools import count

# creates a count iterator object
iterator =(count(start = 0, step = 2))

# prints a even list of integers
print("Even list:",
	list(next(iterator) for _ in range(5)))


# creates a count iterator object
iterator = (count(start = 1, step = 2))

# prints a odd list of integers
print("Odd list:",
	list(next(iterator) for _ in range(5)))

print()

# emulate enumerate()
# using count()

# list containing some strings
my_list =["Ham", "Spam", "Eggs"]

# count spits out integers for
# each value in my list
for i in zip( count(start = 1, step = 1),  my_list ):
	
	# prints tuple in an enumerated
	# format
	print(i)

print()