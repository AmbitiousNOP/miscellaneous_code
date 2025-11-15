#!/usr/bin/env python


class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Cannot be negative')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = '__' + name


class Inventory:
    count = NonNegative()
    weight = NonNegative()

    def __init__(self, name, count, weight):
        self.name = name
        self.count = count
        self.weight = weight

inv1 = Inventory('car1', 2, 234)
#inv2 = Inventory('car1', -2, 234)
inv1.count = 5
print(inv1.name, inv1.count, inv1.weight)
inv1.weight = -4
print()