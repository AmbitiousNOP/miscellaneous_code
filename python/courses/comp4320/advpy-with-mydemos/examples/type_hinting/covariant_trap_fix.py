#!/usr/bin/env python
from animal_kingdom import Move, Mammal, Cat, Dog
from typing import List, Sequence
import operator


def add_cat(mammals: Sequence[Mammal]) -> List[Mammal]:
    # mammals.append(Cat(Move.walk, "semi-longhair with a silky coat"))
    new_col =  operator.add(mammals, [Cat(Move.walk, "semi-longhair with a silky coat")])
    return new_col

cats_and_dogs: List[Mammal] = [Cat(Move.walk, "grey"), Dog(Move.run, "shaggy")]
all_cats: List[Cat] = [Cat(Move.run, "orange"), Cat(Move.walk, "scraggly")]
all_dogs: List[Dog] = [Dog(Move.run, "short and curly"),
                       Dog(Move.walk, "white with black dots")]

cats_and_dogs =add_cat(cats_and_dogs)
all_cats = add_cat(all_cats)                        #mypy error  - no fix for mypy - just need to fix not add non-cat to add_cat
all_dogs = add_cat(all_dogs)                        #mypy error

cats_and_dogs = add_cat(cats_and_dogs)


print()