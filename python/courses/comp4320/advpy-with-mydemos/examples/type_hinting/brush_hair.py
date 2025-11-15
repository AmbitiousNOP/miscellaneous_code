#!/usr/bin/env python
from animal_kingdom import Move, Mammal, Cat, Dog, Animal

class Employee:
    pass

def brush_hair(mammal: Mammal) -> None:
  
    print(f"The {type(mammal).__name__}'s hair is {mammal.hair}")


def main() -> None:
    cat = Cat(Move.walk, "short and grey")
    dog = Dog(Move.run, "long and shaggy")
    brush_hair(cat)
    brush_hair(dog)
    

if __name__ == '__main__':
    main()
