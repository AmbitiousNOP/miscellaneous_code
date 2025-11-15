#!/usr/bin/env python
from animal_kingdom import Move, Mammal, Cat, Dog
from typing import List, Sequence
import operator


def add_cat(mammals: Sequence[Mammal]) -> None:
    # mammals.append(Cat(Move.walk, "semi-longhair with a silky coat"))
    operator.add(mammals, [Cat(Move.walk, "semi-longhair with a silky coat")])


cats_and_dogs: List[Mammal] = [Cat(Move.walk, "grey"), Dog(Move.run, "shaggy")]
all_cats: List[Cat] = [Cat(Move.run, "orange"), Cat(Move.walk, "scraggly")]
all_dogs: List[Dog] = [Dog(Move.run, "short and curly"),
                       Dog(Move.walk, "white with black dots")]

add_cat(cats_and_dogs)
add_cat(all_cats)
add_cat(all_dogs)

add_cat(cats_and_dogs)


print()