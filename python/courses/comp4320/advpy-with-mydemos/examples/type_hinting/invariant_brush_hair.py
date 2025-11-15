#!/usr/bin/env python
from animal_kingdom import Move, Mammal, Cat, Dog
from typing import List


def brush_hair_all(mammals: List[Mammal]) -> None:
    for mammal in mammals:
        print(f"The {type(mammal).__name__}'s hair is {mammal.hair}")
    print()


cats_and_dogs: List[Mammal] = [Cat(Move.walk, "grey"), Dog(Move.run, "shaggy")]
brush_hair_all(cats_and_dogs)

all_cats: List[Cat] = [Cat(Move.run, "orange"), Cat(Move.walk, "scraggly")]
brush_hair_all(all_cats)

all_dogs: List[Dog] = [Dog(Move.run, "short and curly"),
                       Dog(Move.walk, "white with black dots")]
brush_hair_all(all_cats)
