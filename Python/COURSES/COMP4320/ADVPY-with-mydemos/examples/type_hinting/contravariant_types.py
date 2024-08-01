#!/usr/bin/env python
from animal_kingdom import Move, Animal, Mammal, Cat, Dog
from typing import List, Sequence, TypeVar

T_co = TypeVar('T_co', covariant=True)
T_contra = TypeVar('T_contra', contravariant=True)


class ListOrMoreSpecific(List[T_co]):
    pass


class ListOrLessSpecific(List[T_contra]):
    pass

'''
def brush_hair_all(mammals: ListOrMoreSpecific[Mammal]) -> None:
    for mammal in mammals:
        print(f"The {type(mammal).__name__}'s hair is {mammal.hair}")
    print()


def add_cat(mammals: ListOrLessSpecific[Cat]) -> None:
    mammals.append(Cat(Move.walk, "semi-longhair with a soft and silky coat"))


mammals: ListOrMoreSpecific[Mammal] = \
        ListOrMoreSpecific([Cat(Move.walk, "grey"), Dog(Move.run, "shaggy")])

animals: ListOrLessSpecific[Animal] = \
        ListOrLessSpecific([Animal(Move.slither), Cat(Move.walk, "grey"),
                            Dog(Move.run, "shaggy")])

brush_hair_all(mammals)
add_cat(animals)

'''