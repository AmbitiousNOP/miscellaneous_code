#!/usr/bin/env python
from multiple_inheritance import AnimalBase, CanBark, CanFly


class Dog(CanBark, AnimalBase):  # inherit from mixin and primary base class
    #def __init__(self):
    #     super().__init__()
    pass


class Sparrow(CanFly, AnimalBase):  # inherit from mixin and primary base class
    pass


def main():
   # ab = AnimalBase("al")
   # ab.get_id()
    d = Dog('Dennis')
    print(d.get_id())  # Dog inherits get_id() from AnimalBase
    print(d.bark())    # Dog inherits bark() from CanBark mixin
    print()

    s = Sparrow('Steve')
    print(s.get_id())  # Sparrow inherits get_id() from AnimalBase
    print(s.fly())     # Sparrow inherits fly() from CanFly mixin
    print()

    print("Sparrow mro:", Sparrow.mro())
    print()
    print("Dog mro:", Dog.mro())


if __name__ == '__main__':
    main()
