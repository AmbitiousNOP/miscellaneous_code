#!/usr/bin/env python
# (c) 2018 CJ Associates
#
from multiprocessing.dummy import Pool
from datetime import date

with open('../../data/presidents.txt') as pres_in:
    presidents = [tuple(line.rstrip().split(':')) for line in pres_in]


def age_at_inauguration(president):
    birth_date = date(*(int(i) for i in president[3].split('-')))
    inauguration_date = date(*(int(i) for i in president[7].split('-')))
    age = (inauguration_date - birth_date).days / 365.25
    return round(age, 2)


p = Pool(8)

results = p.map(age_at_inauguration, presidents)

print(results, "\n")

print(sorted(results))
print()

average_ages = sum(results)/len(results)
print("average age at inauguration: {:.2f}".format(average_ages))

print
