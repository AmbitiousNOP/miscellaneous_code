#!/usr/bin/env python


class Rabbit:
    # Class data - not duplicated in instances
    LOCATION = "the Cave of Caerbannog"

    def __init__(self, weapon):
        self.weapon = weapon

    # instance method
    def display(self):
        print("This rabbit guarding {} uses {} as a weapon".
              format(Rabbit.LOCATION, self.weapon))

    # The @classmethod decorator makes the function receive the class object,
    # not the instance object
    @classmethod
    def get_location(cls):   # class method
        return cls.LOCATION  # Access class data via cls variable


r = Rabbit("a nice cup of tea")
print(Rabbit.get_location())  # Call class method from the class
print(r.get_location())       # Call class method from the instance
