#!/usr/bin/env python
from __future__ import annotations
from enum import Enum, auto


class Move(Enum):
    walk = auto()  #1
    run = auto()   #2
    slither = auto()
    swim = auto()
    fly = auto()


class Animal:
    def __init__(self: Animal, move: Move):
        self._move = move

    @property
    def move(self) -> Move:
        return self._move


class Mammal(Animal):
    def __init__(self: Mammal, move: Move, hair: str):
        super().__init__(move)
        self._hair = hair

    @property
    def hair(self) -> str:
        return self._hair


class Cat(Mammal):
    pass


class Dog(Mammal):
    pass
