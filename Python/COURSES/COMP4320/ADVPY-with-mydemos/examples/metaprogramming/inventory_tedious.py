#!/usr/bin/env python


class Inventory:
    def __init__(self, name, count, weight):
        self.name = name
        self.count = count
        self.weight = weight

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        if value < 0:
            raise ValueError('Cannot be negative')
        self.__count = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError('Cannot be negative')
        self.__weight = value


inv1 = Inventory('car1', 2, 234)
#inv2 = Inventory('car1', -2, 234)
inv1.count +=1