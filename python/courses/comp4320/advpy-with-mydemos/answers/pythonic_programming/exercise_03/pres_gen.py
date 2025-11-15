#!/usr/bin/python

def pres_upper():
    with open('../../data/presidents.txt') as pres_in:
        for line in pres_in:
            _, last_name, first_name, *_ = line.rstrip().split(':')

            yield f'{first_name} {last_name}'.upper()


for president in pres_upper():
    print(president)
