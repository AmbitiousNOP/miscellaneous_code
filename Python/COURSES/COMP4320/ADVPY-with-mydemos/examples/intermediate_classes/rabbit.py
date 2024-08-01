#!/usr/bin/env python
class Rabbit:

    # self is explicit reference to object implicitly passed by constructor
    def __init__(self, size, danger):
        self._size = size
        self._danger = danger

    # self is explicit reference to object method is called on that is
    # implicitly passed as the first parameter to the method
    def threaten(self):
        print("I am a {} bunny with {}!".format(self._size, self._danger))


# Explicitly passing two arguments to constructor that takes 3 parameters
# The first parameter to constructor is implicitly passed a reference to 'r1'
r1 = Rabbit('large', "sharp, pointy teeth")

# reference to 'r1' is implicitly passses as param to instance method
r1.threaten()

r2 = Rabbit('small', 'fluffy fur')
r2.threaten()
