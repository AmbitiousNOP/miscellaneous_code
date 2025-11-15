#!/usr/bin/env python


def main():

    s = Spam('Mrs. Higgenbotham')  # create instance of class
    s.eggs(1)  # call method

    def scrambled(self):  # define new method outside of class
        print("Hello, {}. Enjoy your scrambled eggs".format(self._name, ))

    setattr(Spam, "eggs", scrambled)  # monkey patch class with the new method

    s.eggs()  # call the monkey-patched method from the instance


class Spam():  # create normal class

    def __init__(self, name):
        self._name = name

    def eggs(self, p1):  # add normal method
        print(f'Good morning, {self._name}. Here are your fried eggs.')


if __name__ == '__main__':

    main()
