"""
Read the file presidents.txt, creating a list of of the presidents' last names.
● Then, use a list comprehension to make a copy of the list of names in upper case.
● Finally, loop through the list returned by the list comprehension and print out the names one per line.

"""

file = "/Users/cjpenn/miscellaneous_code/Python/COURSES/COMP4320/ADVPY-with-mydemos/data/presidents.txt"
with open(file) as f:
    names = ([(i.split(":")[2].upper(), i.split(":")[1].upper())
              for i in (f.read().split("\n")[0:-1])])

for n in names:
    print(*n)
