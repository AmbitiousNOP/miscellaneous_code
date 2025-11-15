#!/usr/bin/env python


def main():
    s = Spam()
    s.eggs("fried")
    print("hasattr()", hasattr(s, 'eggs'))  # check whether attribute exists

    e = getattr(s, 'eggs')                  # retrieve attribute
    e("scrambled")
    setattr(Spam, 'eggs', toast)            # set (or overwrite) attribute
    s.eggs("buttered!")
    delattr(Spam, 'eggs')                   # remove attribute
    print("hasattr()", hasattr(s, 'eggs')) 

class Spam():

    def eggs(self, msg):
        print("eggs!", msg)


def toast(self, msg):
    print("toast!", msg)


if __name__ == '__main__':
    main()
