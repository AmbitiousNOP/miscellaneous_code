#!/usr/bin/env python
class AnimalBase:  # define the primary base/parent class
    def __init__(self, name):
        self._name = name

    def get_id(self):
        return self._name


class CanBark:  # define additional (mixin) base/parent class
    #def __init__(self):
    #    pass
    def bark(self):
        return "woof-woof"


class CanFly:  # define additional (mixin) base/parent class
    def fly(self):
        return "I'm flying"
