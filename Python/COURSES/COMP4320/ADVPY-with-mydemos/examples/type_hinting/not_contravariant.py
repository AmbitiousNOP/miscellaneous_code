#!/usr/bin/env python
from animal_kingdom import Move, Animal, Mammal, Cat, Dog
from typing import List, Sequence
import operator


def add_cat(mammals: List[Mammal]) -> None:
    operator.add(mammals, [Cat(Move.walk, "semi-longhair with a silky coat")])
   

cats_and_dogs: List[Animal] = [Cat(Move.walk, "grey"), Dog(Move.run, "shaggy")]
add_cat(cats_and_dogs)

'''
int small = 4
long big = 8
big = small
small = (int)big
'''