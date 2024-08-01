#!/usr/bin/python

last_names = []
with open('../../data/presidents.txt') as pres_in:
    for line in pres_in:
        last_name = line.split(':')[1]
        last_names.append(last_name)

last_names_upper = [last_name.upper() for last_name in last_names]

for last_name in last_names_upper:
    print(last_name)
