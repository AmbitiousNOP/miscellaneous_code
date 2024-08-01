#!/usr/bin/env python


class Animal:
    count = 0  # defines count as Class data

    def __init__(self, species, name, sound):
        self._species = species
        self._name = name
        self._sound = sound
        Animal.count += 1

    @property
    def species(self):
        return self._species

    @property
    def name(self):
        return self._name

    def make_sound(self):
        return self._sound

    @classmethod        # implicitly passes Class object to remove is called on
    def remove(cls):    # explicitly accepts Class object as cls
        cls.count -= 1  # update class data from Class referenced by cls

    @classmethod
    def zoo_size(cls):
        return cls.count
