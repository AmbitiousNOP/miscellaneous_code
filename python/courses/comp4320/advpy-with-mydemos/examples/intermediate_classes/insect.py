#!/usr/bin/env python

from animal import Animal


class Insect(Animal):
    '''
        An animal with 2 sets of wings and 3 pairs of legs
    '''
    # constructor (AKA initializer)
    def __init__(self, species, name, sound, can_fly=True):
        # pass data shared between parent and child to parent's __init__()
        super().__init__(species, name, sound)
        #Animal.__init__(self,species, name, sound)
        # store what is specific to child class that makes it a special Aniaml
        self._can_fly = can_fly
        self._sets_of_wings = 2
        self._pairs_of_legs = 3

    @property
    def can_fly(self):  # decorated as property getter
        return self._can_fly
