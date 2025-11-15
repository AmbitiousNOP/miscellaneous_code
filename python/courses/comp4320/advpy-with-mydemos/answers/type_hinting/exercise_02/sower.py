#!/usr/bin/env python

from multimethod import multimethod
class Pig:
    pass

class Seed:
    pass

def sow(pig: Pig) -> None:
    print('Oink oink')


def sow(seeds: Seed) -> None:
    print(f'Scatter the {seeds}')
