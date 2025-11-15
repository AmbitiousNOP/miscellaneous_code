"""
Print out all the presidents first and last names, date of birth, and their political affiliations, sorted by date
of birth.
● Read the presidents.txt file, putting the four fields into a list of tuples.
● Loop through the list, sorting by date of birth, and printing the information for each president.
● Use sorted() and a lambda function.
"""

file = "/home/cjpenn/miscellaneous_code/Python/COURSES/COMP4320/ADVPY-with-mydemos/data/presidents.txt"
with open(file) as f:
    names = ([(i.split(":")[2].upper(), i.split(":")[1].upper(), i.split(":")[3].upper(), i.split(":")[-1].upper())
              for i in (f.read().split("\n")[0:-1])])

for i in (sorted(names, key=lambda x: x[2], reverse=True)):
    print(*i)
